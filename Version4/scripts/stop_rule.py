#!/usr/bin/env python3
"""
stop_rule.py - Deterministic convergence gate for Deep Research V4.

The model reports metrics; this script issues the verdict. The model never
grades its own sufficiency (AAC: AI selects parameters, never the action class).

Usage:
  python3 stop_rule.py --log convergence_log.csv --thresholds thresholds.json --mode explore
  python3 stop_rule.py --log convergence_log.csv --thresholds thresholds.json --mode verify

Exit codes: 0 = CONTINUE_EXPLORE / SHIFT_VERIFY, 1 = any STOP_*, 2 = ESCALATE_STUCK, 3 = input error
"""

import argparse
import csv
import json
import sys

DEFAULT_THRESHOLDS = {
    "yield_floor": 0.10,          # net-new claim rate below this = low yield
    "novelty_floor": 0.20,        # new-source rate below this = stale ground
    "window_checkpoints": 2,      # consecutive low-yield checkpoints required
    "flip_alert": 2,              # answer flips within window that signal oscillation
    "gate_coverage_target": 1.0,  # fraction of decision claims at floor required
}

VERDICT_HELP = {
    "STOP_SUFFICIENT": "All decision claims at floor, zero open decision contradictions. Do not gold-plate.",
    "STOP_SATURATED": "Verification budget spent, floors still unmet. Write unmet floors into the residue: the evidence does not exist is a finding.",
    "STOP_BUDGET": "Budget caps hit. Report must include: what we would do with 2x budget.",
    "SHIFT_VERIFY": "Yield is low but gates fail. Stop searching; spend remaining budget verifying.",
    "CONTINUE_EXPLORE": "Still learning and not yet sufficient. Keep searching.",
    "ESCALATE_STUCK": "Answer oscillating with low yield: likely genuine real-world disagreement. Resolver once, then red team, then human. Do not loop.",
}


def load_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("ERROR: convergence log is empty", file=sys.stderr)
        sys.exit(3)
    return rows


def num(row, key, default=0.0):
    try:
        return float(row.get(key, default) or default)
    except ValueError:
        return default


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", required=True)
    ap.add_argument("--thresholds", default=None)
    ap.add_argument("--mode", choices=["explore", "verify"], default="explore")
    ap.add_argument("--budget-exceeded", action="store_true",
                    help="Controller sets this when N_search/N_fetch caps are hit")
    args = ap.parse_args()

    th = dict(DEFAULT_THRESHOLDS)
    if args.thresholds:
        try:
            with open(args.thresholds, encoding="utf-8") as f:
                th.update(json.load(f))
        except FileNotFoundError:
            print(f"NOTE: {args.thresholds} not found, using defaults", file=sys.stderr)

    rows = load_rows(args.log)
    latest = rows[-1]
    w = int(th["window_checkpoints"])
    window = rows[-w:] if len(rows) >= w else rows

    # --- Signals ---------------------------------------------------------
    decision_total = num(latest, "decision_claims_total")
    decision_at_floor = num(latest, "decision_claims_at_floor")
    open_contras = num(latest, "open_decision_contradictions")
    coverage = (decision_at_floor / decision_total) if decision_total > 0 else 0.0

    sufficient = (
        decision_total > 0
        and coverage >= th["gate_coverage_target"]
        and open_contras == 0
    )

    low_yield = len(rows) >= w and all(
        num(r, "new_claim_rate") < th["yield_floor"]
        and num(r, "new_source_rate") < th["novelty_floor"]
        for r in window
    )

    flips = sum(num(r, "answer_flips_window") for r in window)
    stuck = low_yield and flips >= th["flip_alert"]

    # --- Verdict (priority order) ---------------------------------------
    if args.budget_exceeded:
        verdict, code = "STOP_BUDGET", 1
    elif sufficient:
        verdict, code = "STOP_SUFFICIENT", 1
    elif stuck:
        verdict, code = "ESCALATE_STUCK", 2
    elif low_yield and args.mode == "verify":
        verdict, code = "STOP_SATURATED", 1
    elif low_yield:
        verdict, code = "SHIFT_VERIFY", 0
    else:
        verdict, code = "CONTINUE_EXPLORE", 0

    # --- Report ----------------------------------------------------------
    print(f"VERDICT: {verdict}")
    print(f"  gate_coverage: {coverage:.0%} ({int(decision_at_floor)}/{int(decision_total)} decision claims at floor)")
    print(f"  open_decision_contradictions: {int(open_contras)}")
    print(f"  low_yield over last {len(window)} checkpoint(s): {low_yield}")
    print(f"  answer_flips in window: {int(flips)}")
    print(f"  mode: {args.mode}")
    print(f"  action: {VERDICT_HELP[verdict]}")
    sys.exit(code)


if __name__ == "__main__":
    main()
