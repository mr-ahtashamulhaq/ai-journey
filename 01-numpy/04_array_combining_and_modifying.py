import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

combined = np.concatenate((arr1, arr2))
print(combined)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Shape same: ", a.shape == b.shape) # True


original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])

# .vstack(original mat , new row)
with_new_row = np.vstack((original, new_row))
print(original)
print(with_new_row)

# .hstack(original mat , new col)
new_col = np.array([[7], [8]])
with_new_col = np.hstack((original, new_col))
print("With new column", with_new_col)

arr = np.array([1, 2, 3, 4, 5])
deleted = np.delete(arr, 2)
print("Array after deletion: ", deleted)
