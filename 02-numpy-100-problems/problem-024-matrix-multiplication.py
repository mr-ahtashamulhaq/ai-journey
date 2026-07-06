"""
Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
"""

import numpy as np

# np.random.randint(lowest val, high val, size)

mat1 = np.random.randint(1, 20, (5,3))
mat2 = np.random.randint(1, 20, (3,2))
prod = np.matmul(mat1, mat2)
print(prod)
