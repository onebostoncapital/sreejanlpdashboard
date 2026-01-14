from typing import List
from data.price.price_source import PriceSource


class PriceModule:
    """
    PriceModule is responsible for retrieving prices from multiple sources
    using a fallback mechanism.

    It does NOT know where prices come from.
    It only knows how to try sources safely.
    """

    def __init__(self, sources: List[PriceSource]):
        if not sources:
            raise ValueError("At least one PriceSource must be provided")

        self.sources = sources

    def get_current_price(self, symbol: str) -> float:
        """
        Try each price source in order.
        Return the first successful price.
        Raise RuntimeError if all sources fail.
        """
        last_error = None

        for source in self.sources:
            try:
                price = source.get_current_price(symbol)
                if price is None:
                    raise ValueError("PriceSource returned None")
                return price
            except Exception as e:
                last_error = e
                continue

        raise RuntimeError(
            f"All price sources failed for symbol {symbol}. Last error: {last_error}"
        )
