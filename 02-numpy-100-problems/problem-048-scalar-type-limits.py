"""
Print the minimum and maximum representable values for each numpy scalar type
"""

import numpy as np

print(np.iinfo(np.int8))
print(np.iinfo(np.int16))
print(np.iinfo(np.int32))
print(np.iinfo(np.int64))

print(np.finfo(np.float16))
print(np.finfo(np.float32))
print(np.finfo(np.float64))
