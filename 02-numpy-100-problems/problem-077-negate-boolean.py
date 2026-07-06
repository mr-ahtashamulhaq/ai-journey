"""
How to negate a boolean, or to change the sign of a float inplace?
"""

import numpy as np

Z = np.random.randint(0,2,100)
np.logical_not(Z, out=Z)

Z = np.random.uniform(-1.0,1.0,100)
np.negative(Z, out=Z)
