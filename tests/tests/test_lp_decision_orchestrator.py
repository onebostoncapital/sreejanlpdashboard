from core.orchestrator.lp_decision_orchestrator import LPDecisionOrchestrator


def generate_prices(start: float, step: float, count: int):
    return [start + i * step for i in range(count)]


def test_lp_decision_orchestrator_generates_full_report():
    orchestrator = LPDecisionOrchestrator()

    report = orchestrator.generate_report(
        current_price=100.0,
        historical_prices=generate_prices(50.0, 0.2, 250),
        capital_usd=10000,
        leverage=2.0,
        direction="LONG",
    )

    assert "price_context" in report
    assert "technical_analysis" in report
    assert "market_state" in report
    assert "strategy_posture" in report
    assert "liquidity_range" in report
    assert "risk_assessment" in report

    assert report["price_context"]["current_price"] == 100.0
    assert report["strategy_posture"]["posture"] in [
        "AGGRESSIVE",
        "NEUTRAL",
        "DEFENSIVE",
    ]
