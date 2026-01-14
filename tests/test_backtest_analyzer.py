from core.backtesting.backtest_analyzer import BacktestAnalyzer
from core.backtesting.backtest_result import BacktestResult, BacktestStepResult


def dummy_report(posture: str, market_state: str, risk: str, width: float):
    return {
        "market_state": {"market_state": market_state},
        "strategy_posture": {"posture": posture},
        "risk_assessment": {"risk_level": risk},
        "liquidity_range": {"range_width_pct": width},
    }


def test_backtest_analyzer_outputs_metrics():
    results = [
        BacktestStepResult(
            index=1,
            price=100,
            decision_report=dummy_report(
                posture="NEUTRAL",
                market_state="RANGE",
                risk="LOW",
                width=10,
            ),
        ),
        BacktestStepResult(
            index=2,
            price=101,
            decision_report=dummy_report(
                posture="AGGRESSIVE",
                market_state="TRENDING",
                risk="MEDIUM",
                width=6,
            ),
        ),
        BacktestStepResult(
            index=3,
            price=102,
            decision_report=dummy_report(
                posture="AGGRESSIVE",
                market_state="TRENDING",
                risk="MEDIUM",
                width=6,
            ),
        ),
    ]

    backtest = BacktestResult(results=results)

    analyzer = BacktestAnalyzer()
    summary = analyzer.analyze(backtest)

    assert summary["total_steps"] == 3
    assert summary["posture_change_count"] == 1
    assert summary["market_state_distribution"]["TRENDING"] == 2
    assert summary["posture_distribution"]["AGGRESSIVE"] == 2
    assert summary["risk_level_distribution"]["MEDIUM"] == 2
    assert summary["avg_range_width_pct"] == 7.33
