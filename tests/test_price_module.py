"""
Unit tests for the Price Module (v1.0)

Structural tests only.
No external APIs.
"""

import sys
from pathlib import Path

# Ensure project root is on PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from data.price.price_module import PriceModule


def test_price_module_initialization():
    """
    Test that the PriceModule initializes correctly.
    """
    price_module = PriceModule()
    assert price_module is not None


def test_price_module_health_check():
    """
    Test that the PriceModule health check returns True.
    """
    price_module = PriceModule()
    assert price_module.health_check() is True
