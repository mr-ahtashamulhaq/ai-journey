"""
How to find common values between two arrays?
"""

import numpy as np

A = np.array([3,4,7,2,5])
B = np.array([2,7,4,9,0])

print(np.intersect1d(A, B))
