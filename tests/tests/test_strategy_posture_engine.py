from core.strategy.strategy_posture_engine import StrategyPostureEngine


def test_bullish_trend_returns_aggressive_posture():
    engine = StrategyPostureEngine()
    market_state = {
        "state": "TRENDING_BULLISH",
        "confidence": 0.8,
    }

    posture = engine.determine_posture(market_state)

    assert posture.posture == "AGGRESSIVE"
    assert posture.confidence == 0.8


def test_bearish_trend_returns_defensive_posture():
    engine = StrategyPostureEngine()
    market_state = {
        "state": "TRENDING_BEARISH",
        "confidence": 0.7,
    }

    posture = engine.determine_posture(market_state)

    assert posture.posture == "DEFENSIVE"


def test_range_low_volatility_returns_neutral_posture():
    engine = StrategyPostureEngine()
    market_state = {
        "state": "RANGING_LOW_VOLATILITY",
        "confidence": 0.6,
    }

    posture = engine.determine_posture(market_state)

    assert posture.posture == "NEUTRAL"


def test_unknown_state_defaults_to_defensive():
    engine = StrategyPostureEngine()
    market_state = {
        "state": "UNKNOWN",
        "confidence": 0.2,
    }

    posture = engine.determine_posture(market_state)

    assert posture.posture == "DEFENSIVE"
