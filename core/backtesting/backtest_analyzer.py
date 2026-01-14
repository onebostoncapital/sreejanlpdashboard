"""
Backtest Analyzer
=================

Analyzes backtest results to extract descriptive statistics
about system behavior over time.

Version: v1.0
"""

from collections import Counter
from typing import Dict

from core.backtesting.backtest_result import BacktestResult


class BacktestAnalyzer:
    """
    Computes descriptive metrics from backtest outputs.
    """

    def analyze(self, backtest_result: BacktestResult) -> Dict:
        if len(backtest_result) == 0:
            raise ValueError("BacktestResult is empty")

        market_states = []
        postures = []
        risk_levels = []
        range_widths = []

        posture_changes = 0
        last_posture = None

        for step in backtest_result.results:
            report = step.decision_report

            market_states.append(report["market_state"]["market_state"])
            postures.append(report["strategy_posture"]["posture"])
            risk_levels.append(report["risk_assessment"]["risk_level"])
            range_widths.append(report["liquidity_range"]["range_width_pct"])

            current_posture = report["strategy_posture"]["posture"]
            if last_posture is not None and current_posture != last_posture:
                posture_changes += 1
            last_posture = current_posture

        return {
            "total_steps": len(backtest_result),
            "market_state_distribution": dict(Counter(market_states)),
            "posture_distribution": dict(Counter(postures)),
            "risk_level_distribution": dict(Counter(risk_levels)),
            "posture_change_count": posture_changes,
            "avg_range_width_pct": round(
                sum(range_widths) / len(range_widths), 2
            ),
        }
