"""Conversions between ounces and larger imperial weight units"""
OUNCES_PER_POUND = 16.0  # 16 ounces in a pound
OUNCES_PER_STONE = OUNCES_PER_POUND * 14.0  # 14 pounds in a stone

UNITS = ("oz", "lb", "st")


def ounces_to_pounds(x, reverse=False):
    """Convert weights between ounces and pounds.

    Parameters
    ----------
    x : array_like
        Weights in pounds.
    reverse : bool, optional
        If this is set to true this function converts from pounds to ounces
        instead of the default behaviour of ounces to pounds.

    Returns
    -------
    ndarray
        An array of converted weights with the same shape as `x`. If `x` is a
        0-d array, then a scalar is returned.
    """
    if reverse:
        return x * OUNCES_PER_POUND
    else:
        return x / OUNCES_PER_POUND


def ounces_to_stone(x, reverse=False):
    """Convert weights between ounces and stone.

    Parameters
    ----------
    x : array_like
        Weights in stone.
    reverse : bool, optional
        If this is set to true this function converts from stone to ounces
        instead of the default behaviour of ounces to stone.

    Returns
    -------
    ndarray
        An array of converted weights with the same shape as `x`. If `x` is a
        0-d array, then a scalar is returned.
    """
    if reverse:
        return x * OUNCES_PER_STONE
    else:
        return x / OUNCES_PER_STONE
