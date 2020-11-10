import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
rows, cols = np.where(a > 3)
idxs = np.where(a > 3)
print(rows, cols)    # [1 1 1] [0 1 2]
print(idxs)
print(a[idxs])
print(a[a > 3])