"""User-facing functions."""
import numpy as np
from impyrial.utils import check_units
from impyrial.weight.core import (
    UNITS,
    ounces_to_pounds,
    ounces_to_stone,
)


def convert_unit(x, from_unit, to_unit):
    """Convert from one weight unit to another.

    Parameters
    ----------
    x : array_like
        Weights to convert
    from_unit : {'oz', 'lb', 'st'}
        Unit of the input weights `x`
    to_unit : {'oz', 'lb', 'st'}
        Unit of the returned weights

    Returns
    -------
    ndarray
        An array of converted weights with the same shape as `x`. If `x` is a
        0-d array, then a scalar is returned.
    """
    # check if units are valid weight units
    check_units(from_unit, to_unit, UNITS)

    # convert weight to ounces
    if from_unit == "oz":
        ounces = x
    elif from_unit == "lb":
        ounces = ounces_to_pounds(x, reverse=True)
    elif from_unit == "st":
        ounces = ounces_to_stone(x, reverse=True)

    # convert ounces to desired units
    if to_unit == "oz":
        value = ounces
    elif to_unit == "lb":
        value = ounces_to_pounds(ounces)
    elif to_unit == "st":
        value = ounces_to_stone(ounces)

    return value


