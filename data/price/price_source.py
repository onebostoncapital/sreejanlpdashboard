"""
Price Source Interface
======================

Defines the contract that all price sources must follow.

Version: v1.0
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from datetime import datetime


class PriceSource(ABC):
    """
    Abstract base class for all price sources.
    """

    @abstractmethod
    def name(self) -> str:
        """
        Return the human-readable name of the price source.
        """
        pass

    @abstractmethod
    def get_current_price(self, symbol: str) -> Optional[float]:
        """
        Fetch the current price for a trading pair.
        """
        pass

    @abstractmethod
    def get_historical_prices(
        self,
        symbol: str,
        start_time: datetime,
        end_time: datetime,
        interval: str,
    ) -> List[Dict]:
        """
        Fetch historical price data.
        """
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """
        Check whether the price source is operational.
        """
        pass
