"""
Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates
"""

import numpy as np

Z = np.zeros((5,5), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),
                             np.linspace(0,1,5))
print(Z)
