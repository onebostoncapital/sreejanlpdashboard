"""
Liquidity Range Engine
======================

Translates market posture and conditions into a conceptual liquidity range.

This engine does NOT:
- Execute trades
- Allocate capital
- Calculate liquidation

Version: v1.0
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class LiquidityRange:
    lower_bound: float
    upper_bound: float
    range_width_pct: float
    risk_note: str


class LiquidityRangeEngine:
    """
    Computes a conceptual LP price range based on posture and volatility.
    """

    def compute_range(
        self,
        *,
        current_price: float,
        direction: str,
        volatility_label: str,
        posture: str,
        confidence: float,
    ) -> LiquidityRange:

        self._validate_inputs(
            current_price, direction, volatility_label, posture, confidence
        )

        base_width_pct = self._base_width_from_posture(posture)

        volatility_multiplier = {
            "low": 1.0,
            "medium": 1.5,
            "high": 2.0,
        }[volatility_label]

        adjusted_width_pct = base_width_pct * volatility_multiplier

        half_range = current_price * adjusted_width_pct / 100

        if direction == "LONG":
            lower = current_price - half_range
            upper = current_price + half_range * 0.6
        elif direction == "SHORT":
            lower = current_price - half_range * 0.6
            upper = current_price + half_range
        else:  # NEUTRAL
            lower = current_price - half_range
            upper = current_price + half_range

        risk_note = self._risk_note(posture, volatility_label, confidence)

        return LiquidityRange(
            lower_bound=round(lower, 4),
            upper_bound=round(upper, 4),
            range_width_pct=round(adjusted_width_pct, 2),
            risk_note=risk_note,
        )

    def _base_width_from_posture(self, posture: str) -> float:
        mapping = {
            "AGGRESSIVE": 4.0,
            "NEUTRAL": 8.0,
            "DEFENSIVE": 14.0,
        }
        return mapping[posture]

    def _risk_note(self, posture: str, volatility: str, confidence: float) -> str:
        if posture == "AGGRESSIVE" and confidence < 0.6:
            return (
                "Aggressive posture with low confidence increases range breach risk."
            )

        if posture == "DEFENSIVE" and volatility == "high":
            return (
                "Defensive posture recommended due to high volatility environment."
            )

        return "Range reflects current market posture and volatility."

    def _validate_inputs(
        self,
        current_price,
        direction,
        volatility_label,
        posture,
        confidence,
    ):
        if current_price <= 0:
            raise ValueError("current_price must be positive")

        if direction not in {"LONG", "SHORT", "NEUTRAL"}:
            raise ValueError("Invalid direction")

        if volatility_label not in {"low", "medium", "high"}:
            raise ValueError("Invalid volatility_label")

        if posture not in {"AGGRESSIVE", "NEUTRAL", "DEFENSIVE"}:
            raise ValueError("Invalid posture")

        if not (0.0 <= confidence <= 1.0):
            raise ValueError("confidence must be between 0 and 1")
