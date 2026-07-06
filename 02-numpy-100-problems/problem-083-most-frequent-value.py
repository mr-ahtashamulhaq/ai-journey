"""
How to find the most frequent value in an array?
"""

import numpy as np

Z = np.random.randint(0,10,50)
print(np.bincount(Z).argmax())
