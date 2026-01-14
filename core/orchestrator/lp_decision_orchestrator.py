"""
LP Decision Orchestrator
=======================

Coordinates all analytical engines into a single structured LP decision report.

This orchestrator:
- Does NOT execute trades
- Does NOT deploy liquidity
- Does NOT call DeFi protocols

It ONLY assembles intelligence.

Version: v1.0
"""

from typing import Dict, List

from core.ta.ta_engine import TechnicalAnalysisEngine
from core.market_state.market_state_engine import MarketStateEngine
from core.strategy.strategy_posture_engine import StrategyPostureEngine
from core.liquidity.liquidity_range_engine import LiquidityRangeEngine
from core.risk.risk_engine import RiskEngine


class LPDecisionOrchestrator:
    """
    Orchestrates the full LP decision-making pipeline.
    """

    def generate_report(
        self,
        *,
        current_price: float,
        historical_prices: List[float],
        capital_usd: float,
        leverage: float,
        direction: str,
    ) -> Dict:

        # --- Technical Analysis ---
        ta_engine = TechnicalAnalysisEngine(historical_prices)
        ta_summary = ta_engine.summary()

        # --- Market State ---
        market_state_engine = MarketStateEngine(ta_summary)
        market_state_summary = market_state_engine.summary()

        # --- Strategy Posture ---
        posture_engine = StrategyPostureEngine()
        posture = posture_engine.determine_posture(
            {
                "state": market_state_summary["market_state"].upper(),
                "confidence": market_state_summary["confidence"],
            }
        )

        # --- Liquidity Range ---
        range_engine = LiquidityRangeEngine()
        liquidity_range = range_engine.compute_range(
            current_price=current_price,
            direction=direction,
            volatility_label=ta_summary["volatility_label"],
            posture=posture.posture,
            confidence=posture.confidence,
        )

        # --- Risk Assessment ---
        risk_engine = RiskEngine()
        risk = risk_engine.assess_risk(
            current_price=current_price,
            capital_usd=capital_usd,
            leverage=leverage,
            direction=direction,
            confidence=posture.confidence,
        )

        # --- Final Structured Report ---
        return {
            "price_context": {
                "current_price": current_price,
            },
            "technical_analysis": ta_summary,
            "market_state": market_state_summary,
            "strategy_posture": {
                "posture": posture.posture,
                "confidence": posture.confidence,
                "explanation": posture.explanation,
            },
            "liquidity_range": {
                "lower_bound": liquidity_range.lower_bound,
                "upper_bound": liquidity_range.upper_bound,
                "range_width_pct": liquidity_range.range_width_pct,
                "risk_note": liquidity_range.risk_note,
            },
            "risk_assessment": {
                "liquidation_floor_price": risk.liquidation_floor_price,
                "max_adverse_move_pct": risk.max_adverse_move_pct,
                "risk_level": risk.risk_level,
                "explanation": risk.explanation,
            },
        }
