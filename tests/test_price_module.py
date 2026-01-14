import pytest
from datetime import datetime
from typing import List, Dict, Optional

from data.price.price_module import PriceModule
from data.price.price_source import PriceSource


class WorkingPriceSource(PriceSource):
    def name(self) -> str:
        return "WorkingPriceSource"

    def get_current_price(self, symbol: str) -> Optional[float]:
        return 100.0

    def get_historical_prices(
        self,
        symbol: str,
        start_time: datetime,
        end_time: datetime,
        interval: str,
    ) -> List[Dict]:
        return []

    def health_check(self) -> bool:
        return True


class FailingPriceSource(PriceSource):
    def name(self) -> str:
        return "FailingPriceSource"

    def get_current_price(self, symbol: str) -> Optional[float]:
        raise RuntimeError("Source failure")

    def get_historical_prices(
        self,
        symbol: str,
        start_time: datetime,
        end_time: datetime,
        interval: str,
    ) -> List[Dict]:
        raise RuntimeError("Source failure")

    def health_check(self) -> bool:
        return False


class NonePriceSource(PriceSource):
    def name(self) -> str:
        return "NonePriceSource"

    def get_current_price(self, symbol: str) -> Optional[float]:
        return None

    def get_historical_prices(
        self,
        symbol: str,
        start_time: datetime,
        end_time: datetime,
        interval: str,
    ) -> List[Dict]:
        return []

    def health_check(self) -> bool:
        return True


def test_price_module_returns_price_from_first_working_source():
    module = PriceModule(
        sources=[
            WorkingPriceSource(),
            FailingPriceSource(),
        ]
    )

    price = module.get_current_price("SOL-USDC")
    assert price == 100.0


def test_price_module_falls_back_when_first_source_fails():
    module = PriceModule(
        sources=[
            FailingPriceSource(),
            WorkingPriceSource(),
        ]
    )

    price = module.get_current_price("SOL-USDC")
    assert price == 100.0


def test_price_module_raises_error_when_all_sources_fail():
    module = PriceModule(
        sources=[
            FailingPriceSource(),
            NonePriceSource(),
        ]
    )

    with pytest.raises(RuntimeError):
        module.get_current_price("SOL-USDC")
