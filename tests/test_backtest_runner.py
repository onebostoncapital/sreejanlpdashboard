from core.backtesting.backtest_runner import BacktestRunner


def generate_prices(start: float, step: float, count: int):
    return [start + i * step for i in range(count)]


def test_backtest_runner_generates_results():
    prices = generate_prices(50.0, 0.1, 300)

    runner = BacktestRunner()

    result = runner.run(
        historical_prices=prices,
        capital_usd=10000,
        leverage=2.0,
        direction="LONG",
    )

    assert len(result) > 0

    first = result.results[0]

    assert "technical_analysis" in first.decision_report
    assert "market_state" in first.decision_report
    assert "strategy_posture" in first.decision_report
    assert "liquidity_range" in first.decision_report
    assert "risk_assessment" in first.decision_report
