"""
Make an array immutable (read-only)
"""

import numpy as np

Z = np.zeros(10)
Z.flags.writeable = False
