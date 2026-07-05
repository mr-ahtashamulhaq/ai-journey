import numpy as np

# 1-D Slicing same as Python list
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Basic Slicing", arr[2:7])
print("With Step", arr[1:8:2])
print("Negative indexing", arr[-3])

# 2-D Slicing
arr_2d = np.array([[ 1, 2, 3 ],
                   [ 4, 5, 6 ],
                   [ 7, 8, 9 ]])
# [rowTh, colTh]
print("Only one element: ",arr_2d[1,1])
print("Entire Row: ",arr_2d[1])
print("Entire Col: ",arr_2d[:, 1])  # [2 5 8] / first element of every row

arr_2d_unsorted = np.array([[ 3, 1 ],
                            [ 1, 2 ],
                            [ 2, 3 ]])
print("Sorted 2D array by Rows\n", np.sort(arr_2d_unsorted, axis=1))
#  [[1 3]
#  [1 2]
#  [2 3]]
print("Sorted 2D array by Cols\n",np.sort(arr_2d_unsorted, axis=0))
# [[1 1]
#  [2 2]
#  [3 3]]

num = np.array([2,3,10,15,17,4,8,6])
# num[expression to evaluate] - will keep only elements which return true on that expression
print("Even:", num[ num % 2 == 0 ])

# MASK
# we use `mask` key word it stores the expression and evaluate it
mask = num > 5
print("MASK",num[mask]) # will print only numbers that satisfy mask expression

indices = [0, 2, 4]
print(num[indices])

where_res = np.where(num > 10) #return indices where the condition is true
print("WHERE_RES",where_res) # (array([3, 4]),)
print(num[where_res])  # [15 17]

# np.where(condition, if true, if false)
condition_array = np.where(num > 5, num*500,  "false")
print(condition_array)
