"""
Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C?
"""

import numpy as np

C = np.bincount([1,1,2,3,4,4,6])
A = np.repeat(np.arange(len(C)), C)
print(A)
