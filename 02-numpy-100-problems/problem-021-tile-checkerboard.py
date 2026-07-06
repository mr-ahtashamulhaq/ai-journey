"""
Create a checkerboard 8x8 matrix using the tile function
"""

import numpy as np

# np.tile(array, (vertical repetition, horizontal repetition))
block = np.array([
    [0, 1],
    [1, 0]
])

checkerboard = np.tile(block, (4, 4))
print(checkerboard)
