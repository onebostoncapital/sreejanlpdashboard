"""
Backtest Result Models
======================

Defines structured containers for backtesting outputs.

Version: v1.0
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class BacktestStepResult:
    index: int
    price: float
    decision_report: Dict


@dataclass
class BacktestResult:
    results: List[BacktestStepResult]

    def __len__(self):
        return len(self.results)
