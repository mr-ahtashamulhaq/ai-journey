"""
Compute a matrix rank
"""

import numpy as np

Z = np.random.uniform(0,1,(10,10))
U, S, V = np.linalg.svd(Z) # Singular Value Decomposition
threshold = len(S) * S.max() * np.finfo(S.dtype).eps
rank = np.sum(S > threshold)
print(rank)

# alternative solution:

rank = np.linalg.matrix_rank(Z)
print(rank)
