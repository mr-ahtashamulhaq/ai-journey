"""
Consider a 16x16 array, how to get the block-sum (block size is 4x4)?
"""

import numpy as np

Z = np.ones((16,16))
k = 4
S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                                       np.arange(0, Z.shape[1], k), axis=1)
print(S)

# alternative solution:

Z = np.ones((16,16))
k = 4

windows = np.lib.stride_tricks.sliding_window_view(Z, (k, k))
S = windows[::k, ::k, ...].sum(axis=(-2, -1))

# alternative solution (by @Gattocrucco)
S = Z.reshape(4, 4, 4, 4).sum((1, 3))
