from core.market_state.market_state_engine import MarketStateEngine


def test_trending_calm_market():
    ta_summary = {
        "trend": "bullish",
        "volatility": 0.3,
        "volatility_label": "low",
    }

    engine = MarketStateEngine(ta_summary)
    summary = engine.summary()

    assert summary["market_state"] == "trending_calm"
    assert summary["confidence"] > 0.8


def test_trending_volatile_market():
    ta_summary = {
        "trend": "bearish",
        "volatility": 2.5,
        "volatility_label": "high",
    }

    engine = MarketStateEngine(ta_summary)
    summary = engine.summary()

    assert summary["market_state"] == "trending_volatile"


def test_range_bound_calm_market():
    ta_summary = {
        "trend": "neutral",
        "volatility": 0.2,
        "volatility_label": "low",
    }

    engine = MarketStateEngine(ta_summary)
    summary = engine.summary()

    assert summary["market_state"] == "range_bound_calm"


def test_choppy_uncertain_market():
    ta_summary = {
        "trend": "neutral",
        "volatility": 3.0,
        "volatility_label": "high",
    }

    engine = MarketStateEngine(ta_summary)
    summary = engine.summary()

    assert summary["market_state"] == "choppy_uncertain"
    assert summary["confidence"] < 0.5
