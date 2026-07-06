"""
Consider a large vector Z, compute Z to the power of 3 using 3 different methods
"""

import numpy as np

x = np.random.rand(int(5e7))

%timeit np.power(x,3)
%timeit x*x*x
%timeit np.einsum('i,i,i->i',x,x,x)
