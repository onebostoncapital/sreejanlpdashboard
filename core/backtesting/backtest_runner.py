"""
Backtest Runner
===============

Replays historical prices and captures LP decision intelligence at each step.

This runner:
- Does NOT simulate trades
- Does NOT compute PnL
- Does NOT assume correctness

It ONLY records what the system would have decided.

Version: v1.0
"""

from typing import List

from core.orchestrator.lp_decision_orchestrator import LPDecisionOrchestrator
from core.backtesting.backtest_result import BacktestResult, BacktestStepResult


class BacktestRunner:
    """
    Executes a rolling backtest over historical price data.
    """

    def __init__(self):
        self.orchestrator = LPDecisionOrchestrator()

    def run(
        self,
        *,
        historical_prices: List[float],
        capital_usd: float,
        leverage: float,
        direction: str,
        warmup_period: int = 200,
    ) -> BacktestResult:

        if len(historical_prices) <= warmup_period:
            raise ValueError("Not enough historical data for backtesting")

        results = []

        for i in range(warmup_period, len(historical_prices)):
            window_prices = historical_prices[: i + 1]
            current_price = historical_prices[i]

            report = self.orchestrator.generate_report(
                current_price=current_price,
                historical_prices=window_prices,
                capital_usd=capital_usd,
                leverage=leverage,
                direction=direction,
            )

            results.append(
                BacktestStepResult(
                    index=i,
                    price=current_price,
                    decision_report=report,
                )
            )

        return BacktestResult(results=results)
