"""
Create a 8x8 matrix and fill it with a checkerboard pattern
"""

import numpy as np

mat = np.ones((8,8))
mat[::2 , 1::2 ] = 0 # mat[rows you want , col you want]
mat[1::2 , ::2] = 0

print(mat[::1])
