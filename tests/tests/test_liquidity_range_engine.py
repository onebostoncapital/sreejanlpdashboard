import pytest
from core.liquidity.liquidity_range_engine import LiquidityRangeEngine


def test_neutral_range_computation():
    engine = LiquidityRangeEngine()

    result = engine.compute_range(
        current_price=100.0,
        direction="NEUTRAL",
        volatility_label="low",
        posture="NEUTRAL",
        confidence=0.8,
    )

    assert result.lower_bound < 100.0
    assert result.upper_bound > 100.0
    assert result.range_width_pct > 0


def test_aggressive_long_range_is_tighter():
    engine = LiquidityRangeEngine()

    result = engine.compute_range(
        current_price=100.0,
        direction="LONG",
        volatility_label="low",
        posture="AGGRESSIVE",
        confidence=0.9,
    )

    assert result.upper_bound - 100.0 < 100.0 - result.lower_bound


def test_defensive_high_volatility_is_wide():
    engine = LiquidityRangeEngine()

    result = engine.compute_range(
        current_price=100.0,
        direction="NEUTRAL",
        volatility_label="high",
        posture="DEFENSIVE",
        confidence=0.7,
    )

    assert result.range_width_pct >= 20


def test_invalid_inputs_raise_error():
    engine = LiquidityRangeEngine()

    with pytest.raises(ValueError):
        engine.compute_range(
            current_price=-1,
            direction="LONG",
            volatility_label="low",
            posture="AGGRESSIVE",
            confidence=0.5,
        )
