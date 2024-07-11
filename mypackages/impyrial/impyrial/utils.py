"""Basic backend utility functions"""


def check_units(from_unit, to_unit, valid_units):
    """Check whether two units are both in a set.

    Parameters
    ----------
    from_unit : str
    to_unit : str
    valid_units : array_like of str
    """
    if from_unit not in valid_units:
        raise ValueError(f"Unit {from_unit} not in {valid_units}")
    if to_unit not in valid_units:
        raise ValueError(f"Unit {to_unit} not in {valid_units}")
