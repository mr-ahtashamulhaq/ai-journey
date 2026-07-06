"""
How to compute ((A+B)*(-A/2)) in place (without copy)?
"""

import numpy as np

A = np.ones(3)
B = np.ones(3)

np.add(A,B,out=A)
np.divide(A,2,out=A)
np.negative(A, out=A)
np.multiply(A,B,out=A)
