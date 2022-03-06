import numpy as np
A = np.floor(np.random.rand(4,4)*10)
B = np.floor(np.random.rand(4,4)*10)
tmp = np.hstack((B,A))

mat = np.hstack((A,B))
mat = np.vstack((mat, tmp))

print(np.diag(mat))

print(np.resize(np.diag(mat), (2,4)).T)