"""
Dummy Price Source
==================

A fake implementation of PriceSource used for testing and development.

- No APIs
- No internet
- Deterministic behavior

Version: v1.0
"""

from typing import List, Dict, Optional
from datetime import datetime, timedelta

from data.price.price_source import PriceSource


class DummyPriceSource(PriceSource):
    """
    Dummy implementation of a price source.
    """

    def name(self) -> str:
        return "DummyPriceSource"

    def get_current_price(self, symbol: str) -> Optional[float]:
        """
        Return a hard-coded current price.
        """
        if symbol.upper() == "SOL-USDC":
            return 150.0
        return None

    def get_historical_prices(
        self,
        symbol: str,
        start_time: datetime,
        end_time: datetime,
        interval: str,
    ) -> List[Dict]:
        """
        Return fake historical price data.
        """
        if symbol.upper() != "SOL-USDC":
            return []

        prices = []
        current_time = start_time
        price = 140.0

        while current_time <= end_time:
            prices.append(
                {
                    "timestamp": current_time,
                    "open": price,
                    "high": price + 2.0,
                    "low": price - 2.0,
                    "close": price + 1.0,
                }
            )
            current_time += timedelta(hours=1)
            price += 0.5

        return prices

    def health_check(self) -> bool:
        """
        Dummy source is always healthy.
        """
        return True
