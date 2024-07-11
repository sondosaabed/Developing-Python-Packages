from impyrial.weight.core import (
    ounces_to_pounds,
    ounces_to_stone,
)


def test_ounces_to_pounds():
    assert ounces_to_pounds(16) == 1.0
    assert ounces_to_pounds(-1) == -1 / 16.0
    assert ounces_to_pounds(2.5, reverse=True) == 40.0


def test_ounces_to_stone():
    assert ounces_to_stone(224) == 1.0
    assert ounces_to_stone(-14) == -1 / 16.0
    assert ounces_to_stone(3, reverse=True) == 672.0
