import pytest
from core.ta.ta_engine import TechnicalAnalysisEngine


def generate_prices(start: float, step: float, count: int):
    return [start + i * step for i in range(count)]


def test_ma_calculation():
    prices = generate_prices(1.0, 0.1, 250)
    ta = TechnicalAnalysisEngine(prices)

    assert ta.ma_20() > 0
    assert ta.ma_200() > 0


def test_trend_bullish():
    prices = generate_prices(1.0, 0.2, 250)
    ta = TechnicalAnalysisEngine(prices)

    assert ta.trend_direction() == "bullish"


def test_trend_bearish():
    prices = list(reversed(generate_prices(1.0, 0.2, 250)))
    ta = TechnicalAnalysisEngine(prices)

    assert ta.trend_direction() == "bearish"


def test_volatility_label():
    prices = generate_prices(100.0, 0.01, 250)
    ta = TechnicalAnalysisEngine(prices)

    assert ta.volatility_label() in ["low", "medium", "high"]


def test_summary_keys():
    prices = generate_prices(1.0, 0.1, 250)
    ta = TechnicalAnalysisEngine(prices)

    summary = ta.summary()

    assert "ma_20" in summary
    assert "ma_200" in summary
    assert "trend" in summary
    assert "volatility" in summary
    assert "volatility_label" in summary
