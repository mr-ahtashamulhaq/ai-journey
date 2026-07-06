"""
Find the nearest value from a given value in an array
"""

import numpy as np

Z = np.random.uniform(0,1,10)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)
