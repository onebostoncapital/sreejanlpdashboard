"""
Price Module
============

Coordinates access to price data using one or more price sources.

Version: v1.0 (Dummy source wired)
"""

from typing import List, Dict, Optional
from datetime import datetime

from data.price.price_source import PriceSource


class PriceModule:
    """
    PriceModule provides access to current and historical prices.
    """

    def __init__(self, sources: Optional[List[PriceSource]] = None) -> None:
        """
        Initialize the Price Module.

        Args:
            sources (List[PriceSource], optional): Ordered list of price sources
        """
        self.sources: List[PriceSource] = sources or []

    def get_current_price(self, symbol: str) -> Optional[float]:
        """
        Get the current price from the first healthy source
        that returns a valid price.
        """
        for source in self.sources:
            if not source.health_check():
                continue

            price = source.get_current_price(symbol)
            if price is not None:
                return price

        return None

    def get_historical_prices(
        self,
        symbol: str,
        start_time: datetime,
        end_time: datetime,
        interval: str,
    ) -> List[Dict]:
        """
        Get historical prices from the first healthy source
        that returns data.
        """
        for source in self.sources:
            if not source.health_check():
                continue

            data = source.get_historical_prices(
                symbol, start_time, end_time, interval
            )
            if data:
                return data

        return []

    def health_check(self) -> bool:
        """
        Price module is healthy if at least one source is healthy.
        """
        return any(source.health_check() for source in self.sources)
