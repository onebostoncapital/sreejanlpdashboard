"""
Risk & Liquidation Floor Engine
===============================

Provides a conservative risk-awareness layer for leveraged LP positions.

This engine does NOT:
- Execute trades
- Interact with DeFi protocols
- Calculate exact liquidation prices

It ONLY answers:
"Where does risk become unacceptable given leverage and capital?"

Version: v1.0
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class RiskAssessment:
    liquidation_floor_price: float
    max_adverse_move_pct: float
    risk_level: str
    explanation: str


class RiskEngine:
    """
    Computes conservative risk boundaries for LP positions.
    """

    def assess_risk(
        self,
        *,
        current_price: float,
        capital_usd: float,
        leverage: float,
        direction: str,
        confidence: float,
    ) -> RiskAssessment:

        self._validate_inputs(
            current_price, capital_usd, leverage, direction, confidence
        )

        # Conservative max adverse move model
        base_adverse_pct = 50.0 / leverage

        # Adjust based on confidence (lower confidence → tighter risk)
        adjusted_adverse_pct = base_adverse_pct * confidence

        adverse_move = current_price * adjusted_adverse_pct / 100

        if direction == "LONG":
            liquidation_floor = current_price - adverse_move
        elif direction == "SHORT":
            liquidation_floor = current_price + adverse_move
        else:
            liquidation_floor = current_price

        risk_level = self._risk_level(adjusted_adverse_pct)

        explanation = (
            f"With {leverage}x leverage and confidence {confidence:.2f}, "
            f"the system allows a maximum adverse move of "
            f"{adjusted_adverse_pct:.2f}% before risk becomes unacceptable."
        )

        return RiskAssessment(
            liquidation_floor_price=round(liquidation_floor, 4),
            max_adverse_move_pct=round(adjusted_adverse_pct, 2),
            risk_level=risk_level,
            explanation=explanation,
        )

    def _risk_level(self, adverse_pct: float) -> str:
        if adverse_pct < 10:
            return "HIGH"
        if adverse_pct < 20:
            return "MEDIUM"
        return "LOW"

    def _validate_inputs(
        self,
        current_price,
        capital_usd,
        leverage,
        direction,
        confidence,
    ):
        if current_price <= 0:
            raise ValueError("current_price must be positive")

        if capital_usd <= 0:
            raise ValueError("capital_usd must be positive")

        if leverage <= 1:
            raise ValueError("leverage must be greater than 1")

        if direction not in {"LONG", "SHORT"}:
            raise ValueError("direction must be LONG or SHORT")

        if not (0.0 <= confidence <= 1.0):
            raise ValueError("confidence must be between 0 and 1")
