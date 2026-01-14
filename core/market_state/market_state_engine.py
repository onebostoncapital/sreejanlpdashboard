from typing import Dict


class MarketStateEngine:
    """
    Interprets technical analysis outputs into a human-readable market state.
    """

    def __init__(self, ta_summary: Dict):
        required_keys = {
            "trend",
            "volatility",
            "volatility_label",
        }

        if not required_keys.issubset(ta_summary.keys()):
            raise ValueError("TA summary missing required fields")

        self.ta = ta_summary

    def market_state(self) -> str:
        trend = self.ta["trend"]
        volatility_label = self.ta["volatility_label"]

        if trend in ["bullish", "bearish"] and volatility_label == "low":
            return "trending_calm"

        if trend in ["bullish", "bearish"] and volatility_label in ["medium", "high"]:
            return "trending_volatile"

        if trend == "neutral" and volatility_label == "low":
            return "range_bound_calm"

        return "choppy_uncertain"

    def confidence(self) -> float:
        """
        Confidence score between 0 and 1.
        Higher when signals agree, lower when mixed.
        """
        trend = self.ta["trend"]
        volatility_label = self.ta["volatility_label"]

        if trend in ["bullish", "bearish"] and volatility_label == "low":
            return 0.85

        if trend in ["bullish", "bearish"] and volatility_label in ["medium", "high"]:
            return 0.65

        if trend == "neutral" and volatility_label == "low":
            return 0.75

        return 0.4

    def explanation(self) -> str:
        state = self.market_state()

        explanations = {
            "trending_calm": (
                "The market is trending with low volatility. "
                "Price direction is clear and movements are controlled."
            ),
            "trending_volatile": (
                "The market shows a clear trend but with elevated volatility. "
                "Direction exists, but risk is higher due to large swings."
            ),
            "range_bound_calm": (
                "The market is moving sideways with low volatility. "
                "No strong directional bias is present."
            ),
            "choppy_uncertain": (
                "Market signals are mixed or unstable. "
                "Direction is unclear and conditions are unpredictable."
            ),
        }

        return explanations[state]

    def summary(self) -> Dict:
        return {
            "market_state": self.market_state(),
            "confidence": self.confidence(),
            "explanation": self.explanation(),
        }
