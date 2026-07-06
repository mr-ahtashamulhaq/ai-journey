"""
Create random vector of size 10 and replace the maximum value by 0
"""

import numpy as np

V = np.random.randint(1,100,(10))
print(V)
ans = np.where(V == np.max(V) , 0, V)
print(ans)
