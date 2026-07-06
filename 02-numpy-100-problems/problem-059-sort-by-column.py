"""
How to sort an array by the nth column?
"""

import numpy as np

Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])
