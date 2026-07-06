"""
Create a 10x10 array with random values and find the minimum and maximum values
"""

import numpy as np

mat = np.random.random((10,10))
min_mat = mat.min()
max_mat = mat.max()
print(min_mat)
print(max_mat)
