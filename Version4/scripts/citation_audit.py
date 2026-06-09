#!/usr/bin/env python3
"""
citation_audit.py - Deterministic citation gate for Deep Research V4.

Checks that every inline [E###] reference in the report resolves to an evidence
ledger row that meets its tier floor, and (optionally, with --fetch) that the
ledger quote still exists at the cited URL.

This replaces model self-review for citations. The script's exit code is the gate.

Usage:
  python3 citation_audit.py --ledger 04_evidence_ledger.csv --report 08_report/ \
      --out 09_qa/citation_audit.md [--fetch] [--timeout 15]

Exit codes: 0 = PASS, 1 = FAIL, 3 = input error
"""

import argparse
import csv
import os
import re
import sys
import urllib.request

CLAIM_REF = re.compile(r"\[(E\d{3,4})(?:\s*,\s*E\d{3,4})*\]")
SINGLE_ID = re.compile(r"E\d{3,4}")

FLOORS = {"context": 0.60, "finding": 0.80, "decision": 0.92}
MIN_GROUPS = {"context": 1, "finding": 2, "decision": 2}  # finding: 2 groups OR 1 primary (quality A)


def load_ledger(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            rows = {r["claim_id"].strip(): r for r in csv.DictReader(f) if r.get("claim_id")}
    except FileNotFoundError:
        print(f"ERROR: ledger not found: {path}", file=sys.stderr)
        sys.exit(3)
    if not rows:
        print("ERROR: ledger has no rows", file=sys.stderr)
        sys.exit(3)
    return rows


def collect_refs(report_dir):
    refs = {}  # claim_id -> [(file, line_no)]
    for root, _, files in os.walk(report_dir):
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            p = os.path.join(root, name)
            with open(p, encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    for m in CLAIM_REF.finditer(line):
                        for cid in SINGLE_ID.findall(m.group(0)):
                            refs.setdefault(cid, []).append((name, i))
    return refs


def norm(text):
    return re.sub(r"\s+", " ", (text or "")).strip().lower()


def quote_live(url, quote, timeout):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (citation-audit)"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(2_000_000).decode("utf-8", errors="ignore")
        page = norm(re.sub(r"<[^>]+>", " ", body))
        q = norm(quote)
        if not q:
            return "NO_QUOTE"
        if q in page:
            return "OK"
        # fallback: 8-word shingle match survives minor markup differences
        words = q.split()
        if len(words) >= 8:
            for s in range(0, len(words) - 7, 4):
                if " ".join(words[s:s + 8]) in page:
                    return "OK"
        return "QUOTE_NOT_FOUND"
    except Exception as e:
        return f"FETCH_ERROR:{type(e).__name__}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--report", required=True)
    ap.add_argument("--out", default="citation_audit.md")
    ap.add_argument("--fetch", action="store_true", help="Re-fetch URLs and confirm quotes live")
    ap.add_argument("--timeout", type=int, default=15)
    args = ap.parse_args()

    ledger = load_ledger(args.ledger)
    refs = collect_refs(args.report)
    failures, warnings, checked = [], [], 0

    for cid, locs in sorted(refs.items()):
        where = f"{locs[0][0]}:{locs[0][1]}" + (f" (+{len(locs)-1} more)" if len(locs) > 1 else "")
        row = ledger.get(cid)
        if row is None:
            failures.append(f"{cid} cited at {where}: NOT IN LEDGER")
            continue
        checked += 1
        tier = (row.get("tier") or "context").strip().lower()
        status = (row.get("status") or "").strip().lower()
        try:
            conf = float(row.get("confidence") or 0)
        except ValueError:
            conf = 0.0
        groups = len({g.strip() for g in (row.get("independence_group") or "").split(";") if g.strip()})
        quality = (row.get("source_quality") or "").strip().upper()

        if tier in ("finding", "decision") and status != "verified":
            failures.append(f"{cid} ({tier}) at {where}: status={status or 'missing'} (must be verified)")
        if conf < FLOORS.get(tier, 0.6):
            failures.append(f"{cid} ({tier}) at {where}: confidence {conf:.2f} below floor {FLOORS[tier]:.2f}")
        need = MIN_GROUPS.get(tier, 1)
        if groups < need and not (tier == "finding" and quality.startswith("A")):
            failures.append(f"{cid} ({tier}) at {where}: {groups} independence group(s), needs {need}")
        if not (row.get("url") or "").strip():
            failures.append(f"{cid} at {where}: no URL in ledger")
        elif args.fetch and tier in ("finding", "decision"):
            res = quote_live(row["url"].strip(), row.get("quote", ""), args.timeout)
            if res == "QUOTE_NOT_FOUND":
                failures.append(f"{cid} at {where}: quote not found live at {row['url']}")
            elif res != "OK":
                warnings.append(f"{cid}: live check inconclusive ({res}) at {row['url']}")

    # Decision-tier ledger claims never cited anywhere = orphaned conclusions
    cited = set(refs)
    orphans = [cid for cid, r in ledger.items()
               if (r.get("tier") or "").strip().lower() == "decision"
               and (r.get("status") or "").lower() == "verified" and cid not in cited]
    for cid in orphans:
        warnings.append(f"{cid}: verified decision claim never cited in report")

    verdict = "PASS" if not failures else "FAIL"
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(f"# Citation Audit: {verdict}\n\n")
        f.write(f"- Claims cited in report: {len(refs)}\n")
        f.write(f"- Ledger rows checked: {checked}\n")
        f.write(f"- Failures: {len(failures)}\n- Warnings: {len(warnings)}\n")
        f.write(f"- Live fetch: {'on' if args.fetch else 'off'}\n\n")
        if failures:
            f.write("## Failures (gate-blocking)\n\n")
            f.writelines(f"- {x}\n" for x in failures)
            f.write("\n")
        if warnings:
            f.write("## Warnings\n\n")
            f.writelines(f"- {x}\n" for x in warnings)

    print(f"CITATION AUDIT: {verdict} ({len(failures)} failures, {len(warnings)} warnings) -> {args.out}")
    sys.exit(0 if verdict == "PASS" else 1)


if __name__ == "__main__":
    main()
