import pytest
from core.risk.risk_engine import RiskEngine


def test_long_position_liquidation_floor_below_price():
    engine = RiskEngine()

    result = engine.assess_risk(
        current_price=100.0,
        capital_usd=10000,
        leverage=2.0,
        direction="LONG",
        confidence=0.8,
    )

    assert result.liquidation_floor_price < 100.0
    assert result.max_adverse_move_pct > 0


def test_short_position_liquidation_floor_above_price():
    engine = RiskEngine()

    result = engine.assess_risk(
        current_price=100.0,
        capital_usd=10000,
        leverage=2.0,
        direction="SHORT",
        confidence=0.8,
    )

    assert result.liquidation_floor_price > 100.0


def test_low_confidence_increases_risk():
    engine = RiskEngine()

    high_conf = engine.assess_risk(
        current_price=100.0,
        capital_usd=10000,
        leverage=2.0,
        direction="LONG",
        confidence=0.9,
    )

    low_conf = engine.assess_risk(
        current_price=100.0,
        capital_usd=10000,
        leverage=2.0,
        direction="LONG",
        confidence=0.4,
    )

    assert low_conf.max_adverse_move_pct < high_conf.max_adverse_move_pct


def test_invalid_inputs_raise_error():
    engine = RiskEngine()

    with pytest.raises(ValueError):
        engine.assess_risk(
            current_price=-1,
            capital_usd=10000,
            leverage=2.0,
            direction="LONG",
            confidence=0.5,
        )
