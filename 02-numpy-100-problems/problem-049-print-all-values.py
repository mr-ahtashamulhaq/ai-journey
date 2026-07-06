"""
How to print all the values of an array?
"""

import numpy as np

X = np.arange(100000)
np.set_printoptions(threshold=float("inf"))
print(X)
