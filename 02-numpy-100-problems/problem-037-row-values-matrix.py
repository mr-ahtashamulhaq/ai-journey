"""
Create a 5x5 matrix with row values ranging from 0 to 4
"""

import numpy as np

row = np.arange(5)
matii = np.tile(row,(5,1))

print(matii)
