"""
Consider an array of dimension (5,5,3), how to multiply it by an array with dimensions (5,5)?
"""

import numpy as np

A = np.ones((5,5,3))
B = 2*np.ones((5,5))
print(A * B[:,:,None])
