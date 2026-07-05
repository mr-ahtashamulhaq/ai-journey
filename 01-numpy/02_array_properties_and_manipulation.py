import numpy as np

# PROPERTIES OF ARRAYS
np_arr = np.array([[1,2,3],
                  [4,5,6]])
print("Shape: ", np_arr.shape)
print("Dimensions: ", np_arr.ndim)
print("Size: ", np_arr.size)
print("DType: ", np_arr.dtype)

# Shape:  (2, 3)
# Dimensions:  2
# Size:  6
# DType:  int64

arr = np.arange(15)
print("\nOrg:", arr)

reshaped = arr.reshape((3,5))
print("\nReshaped:",reshaped)

flattened = reshaped.flatten()
print("\nflatten:", flattened)

raveled = reshaped.ravel()
print("\nRavel:", raveled)

trans = reshaped.T
print("\nTranspose:\n",trans)
