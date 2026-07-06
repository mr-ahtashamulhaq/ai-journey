"""
Create a 2d array with 1 on the border and 0 inside
"""

import numpy as np

ones = np.ones((5,5))
ones[1:-1,1:-1] = 0
print(ones)
