import numpy as np

#mat = np.floor(np.random.random_integers(4,5)*12)
mat = np.random.randint(0, 12, size=(4, 5))
print(mat)

# Sum rows
print(np.sum(mat, axis = 1))

# Sum cols
print(np.sum(mat, axis = 0))

# Sum even cols
print(np.sum(mat[:,::2], axis = 0))

# Mean of columns
print(np.mean(mat, axis = 0))

# Mean of matrix
print(np.mean(mat))