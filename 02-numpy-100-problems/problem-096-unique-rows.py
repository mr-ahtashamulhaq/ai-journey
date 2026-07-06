"""
Given a two dimensional array, how to extract unique rows?
"""

import numpy as np

Z = np.random.randint(0,2,(6,3))
T = np.ascontiguousarray(Z).view(np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))
_, idx = np.unique(T, return_index=True)
uZ = Z[idx]
print(uZ)

# NumPy >= 1.13
uZ = np.unique(Z, axis=0)
print(uZ)
