from typing import List, Dict
import statistics


class TechnicalAnalysisEngine:
    """
    Pure Technical Analysis engine.

    Input: list of historical close prices (floats)
    Output: numeric indicators + human-readable labels
    """

    def __init__(self, prices: List[float]):
        if len(prices) < 200:
            raise ValueError("At least 200 price points are required")

        self.prices = prices

    def moving_average(self, period: int) -> float:
        return sum(self.prices[-period:]) / period

    def ma_20(self) -> float:
        return self.moving_average(20)

    def ma_200(self) -> float:
        return self.moving_average(200)

    def trend_direction(self) -> str:
        ma20 = self.ma_20()
        ma200 = self.ma_200()

        if ma20 > ma200:
            return "bullish"
        elif ma20 < ma200:
            return "bearish"
        else:
            return "neutral"

    def volatility(self) -> float:
        """
        Simple volatility: standard deviation of last 20 closes
        """
        return statistics.stdev(self.prices[-20:])

    def volatility_label(self) -> str:
        vol = self.volatility()

        if vol < 0.5:
            return "low"
        elif vol < 2.0:
            return "medium"
        else:
            return "high"

    def summary(self) -> Dict:
        return {
            "ma_20": self.ma_20(),
            "ma_200": self.ma_200(),
            "trend": self.trend_direction(),
            "volatility": self.volatility(),
            "volatility_label": self.volatility_label(),
        }
