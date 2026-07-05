import numpy as np

# create array from list
arr_1d = np.array([1,2,3,4])
print(arr_1d)

# create 2d array
arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("\n2d Array : \n",arr_2d)

# MULTIPLICATION
# Simple List
sim_list = [1,2,3]
print("\n", sim_list * 2) #  [1, 2, 3, 1, 2, 3]

# Numpy Array
print("\n", arr_1d * 2) # [2 4 6 8]

# CREATING ARRAY FROM SCRATCH
# Numpy .arange(start, stop, step)
np_array = np.arange(10)
print("\nseq\n",np_array) # [0 1 2 3 4 5 6 7 8 9]

np_array = np.arange(0,10)
print("\nseq\n",np_array) # [0 1 2 3 4 5 6 7 8 9]

np_array = np.arange(0,10, 2)
print("\nskip sequence\n",np_array) # [0 2 4 6 8]

# Numpy .zeros((rows, cols))
zeros = np.zeros((2,3))
print("\nZeros\n",zeros) # [[0. 0. 0.], [0. 0. 0.]]

ones = np.ones((2,4))
print("\nOnes\n",ones) # [[1. 1. 1. 1.],[1. 1. 1. 1.]]

full = np.full((2,3), 5)
print("\nFull\n",full) # [[5 5 5],[5 5 5]]

# TENSOR (n dimension matrix)
tensy = np.array([[[1,2],[3,4]],
                 [[5,6], [7,8]]])
print("\nTensor\n",tensy)
