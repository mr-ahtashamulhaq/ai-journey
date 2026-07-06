"""
How to sum a small array faster than np.sum?
"""

import numpy as np

Z = np.arange(10)
np.add.reduce(Z)
