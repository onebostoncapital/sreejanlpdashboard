"""
DeFiTuna Adapter (Constraint Model)
==================================

Translates conceptual LP ranges into protocol-valid ranges
using conservative, protocol-style safety rules.

Version: v1.2
"""

from dataclasses import dataclass


@dataclass
class ProtocolValidatedRange:
    lower_bound: float
    upper_bound: float
    is_valid: bool
    notes: str


class DeFiTunaAdapter:
    """
    Applies protocol-style constraints to liquidity ranges.
    """

    MIN_RANGE_WIDTH_PCT = 2.0
    SAFETY_BUFFER_PCT = 5.0
    EPSILON = 1e-6  # floating point safety margin

    def validate_range(
        self,
        *,
        lower_bound: float,
        upper_bound: float,
        current_price: float,
        liquidation_floor: float,
        direction: str,
    ) -> ProtocolValidatedRange:

        if lower_bound <= 0 or upper_bound <= 0:
            return ProtocolValidatedRange(
                lower_bound,
                upper_bound,
                False,
                "Invalid price bounds (must be positive)",
            )

        width_pct = (upper_bound - lower_bound) / current_price * 100

        # STRICT + FLOAT-SAFE CHECK
        if width_pct <= self.MIN_RANGE_WIDTH_PCT + self.EPSILON:
            return ProtocolValidatedRange(
                lower_bound,
                upper_bound,
                False,
                "Range too narrow for protocol safety",
            )

        if direction == "LONG":
            safety_limit = liquidation_floor * (1 + self.SAFETY_BUFFER_PCT / 100)
            if lower_bound <= safety_limit:
                return ProtocolValidatedRange(
                    lower_bound,
                    upper_bound,
                    False,
                    "Lower bound too close to liquidation floor",
                )

        if direction == "SHORT":
            safety_limit = liquidation_floor * (1 - self.SAFETY_BUFFER_PCT / 100)
            if upper_bound >= safety_limit:
                return ProtocolValidatedRange(
                    lower_bound,
                    upper_bound,
                    False,
                    "Upper bound too close to liquidation floor",
                )

        return ProtocolValidatedRange(
            lower_bound=round(lower_bound, 4),
            upper_bound=round(upper_bound, 4),
            is_valid=True,
            notes="Range valid under conservative DeFiTuna constraints",
        )
