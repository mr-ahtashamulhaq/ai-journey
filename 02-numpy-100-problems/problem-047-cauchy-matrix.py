"""
Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))
"""

import numpy as np

X = np.array([1,2,3])
Y = np.array([4,5])

C = 1 / (X[:, None] - Y)
print(C)
