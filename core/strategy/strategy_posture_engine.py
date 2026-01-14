"""
Strategy Posture Engine
=======================

Maps market states to liquidity provider behavioral posture.

This engine does NOT:
- Place liquidity
- Choose ranges
- Forecast price

It ONLY answers:
"How aggressive or defensive should a liquidity provider be?"

Version: v1.0
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class StrategyPosture:
    posture: str
    confidence: float
    explanation: str


class StrategyPostureEngine:
    """
    Determines LP behavioral posture based on market state.
    """

    def determine_posture(self, market_state: Dict) -> StrategyPosture:
        state = market_state.get("state")
        confidence = market_state.get("confidence", 0.0)

        if state == "TRENDING_BULLISH":
            return StrategyPosture(
                posture="AGGRESSIVE",
                confidence=confidence,
                explanation=(
                    "Market is trending bullish with directional clarity. "
                    "More aggressive liquidity positioning may be acceptable."
                ),
            )

        if state == "TRENDING_BEARISH":
            return StrategyPosture(
                posture="DEFENSIVE",
                confidence=confidence,
                explanation=(
                    "Market is trending bearish. Downside risk is elevated, "
                    "defensive liquidity behavior is recommended."
                ),
            )

        if state == "RANGING_LOW_VOLATILITY":
            return StrategyPosture(
                posture="NEUTRAL",
                confidence=confidence,
                explanation=(
                    "Market is range-bound with low volatility. "
                    "Neutral liquidity positioning is appropriate."
                ),
            )

        if state == "RANGING_HIGH_VOLATILITY":
            return StrategyPosture(
                posture="DEFENSIVE",
                confidence=confidence,
                explanation=(
                    "Market is choppy with high volatility. "
                    "Wide or cautious liquidity behavior is recommended."
                ),
            )

        return StrategyPosture(
            posture="DEFENSIVE",
            confidence=confidence,
            explanation=(
                "Market state is unclear or low confidence. "
                "Defaulting to defensive behavior."
            ),
        )
