"""
Find indices of non-zero elements from [1,2,0,0,4,0]
"""

import numpy as np

v = np.array([1,2,0,0,4,0])
wh_res = np.where(v != 0)
print(wh_res)
way_2 = np.nonzero(v)
print(way_2)
