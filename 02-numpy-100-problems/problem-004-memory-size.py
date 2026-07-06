"""
How to find the memory size of any array
"""

import numpy as np

# .item_size() return memory size of each item of array
# .size() return length or numbers of element  in array
# .nbytes return memory size of complete array

arr = np.arange(10, dtype='int8') #create 10 element array in which each element wil be 8 bits
print(arr)
print("Memory Size : ", arr.size * arr.itemsize)
print("Memory Size : ", arr.nbytes)
