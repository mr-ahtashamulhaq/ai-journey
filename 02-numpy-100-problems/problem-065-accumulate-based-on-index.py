"""
How to accumulate elements of a vector (X) to an array (F) based on an index list (I)?
"""

import numpy as np

X = [1,2,3,4,5,6]
I = [1,3,9,3,4,1]
F = np.bincount(I,X)
print(F)
