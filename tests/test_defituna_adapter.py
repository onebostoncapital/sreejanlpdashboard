from core.protocols.defituna_adapter import DeFiTunaAdapter


def test_valid_range_passes_validation():
    adapter = DeFiTunaAdapter()

    result = adapter.validate_range(
        lower_bound=90,
        upper_bound=120,
        current_price=100,
        liquidation_floor=70,
        direction="LONG",
    )

    assert result.is_valid is True


def test_range_too_narrow_fails():
    adapter = DeFiTunaAdapter()

    result = adapter.validate_range(
        lower_bound=99,
        upper_bound=101,
        current_price=100,
        liquidation_floor=70,
        direction="LONG",
    )

    assert result.is_valid is False


def test_range_too_close_to_liquidation_fails():
    adapter = DeFiTunaAdapter()

    result = adapter.validate_range(
        lower_bound=72,
        upper_bound=120,
        current_price=100,
        liquidation_floor=70,
        direction="LONG",
    )

    assert result.is_valid is False
