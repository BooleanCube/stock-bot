import math
import numpy as np

def float_factorial(n: int) -> float:
    return float(math.factorial(n)) if n < 171 else np.inf

def pythagorean_distance(pt1, pt2):
    a_sq = (pt2[0] - pt1[0]) ** 2
    b_sq = (pt2[1] - pt1[1]) ** 2
    return math.sqrt(a_sq + b_sq)

def axis_slice(a, start=None, stop=None, step=None, axis=-1):
    a_slice = [slice(None)] * a.ndim
    a_slice[axis] = slice(start, stop, step)
    b = a[tuple(a_slice)]
    return b