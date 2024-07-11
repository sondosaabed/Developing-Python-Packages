import numpy as np


def calculate_hypotenuse(side1, side2):
    """Calculate the length of the hypotenuse."""
    l = np.sqrt( side1**2 + side2**2 )  # ____: ____
    return l

### solution
import numpy as np


def calculate_hypotenuse(side1, side2):
    """Calculate the length of the hypotenuse."""
    l = np.sqrt(side1**2 + side2**2)  # noqa: E741
    return l
