"""
Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area
"""

import numpy as np

Z = np.zeros((10,10), dtype=[('x', float), ('y', float)])

Z['x'] = np.linspace(0,1,10)
Z['y'] = np.linspace(0,1,10).reshape(-1,1)

print(Z)
