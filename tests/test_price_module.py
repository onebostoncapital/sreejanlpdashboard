"""
Unit tests for PriceModule using DummyPriceSource.

These tests validate end-to-end price access without any external APIs.
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta

# Ensure project root is on PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from data.price.price_module import PriceModule
from data.price.dummy_price_source import DummyPriceSource


def test_get_current_price_from_dummy_source():
    source = DummyPriceSource()
    module = PriceModule(sources=[source])

    price = module.get_current_price("SOL-USDC")
    assert price == 150.0


def test_get_historical_prices_from_dummy_source():
    source = DummyPriceSource()
    module = PriceModule(sources=[source])

    start_time = datetime.now() - timedelta(hours=3)
    end_time = datetime.now()

    data = module.get_historical_prices(
        "SOL-USDC",
        start_time,
        end_time,
        interval="1h",
    )

    assert isinstance(data, list)
    assert len(data) > 0
