"""
How to add a border (filled with 0's) around an existing array?
"""

import numpy as np

randos = np.random.random((5,5))
randos[:,[0,-1]] = 0
randos[[0,-1],:] = 0
print(randos)
