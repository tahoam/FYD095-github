import numpy as np

mat = np.floor(np.random.rand(4,5)*12)
print(mat)

row, col = mat.shape

# Sum rows
for row in range(row):
    print(sum(mat[row,:]))
print()

# Sum columns
tmp = []
for col in range(col):
    tmp.append(sum(mat[:,col]))
print(tmp)
print()

# Sum even columns
tmp = []
for col in range(col):
    if col % 2 == 0:
        tmp.append(sum(mat[:,col]))
print(tmp)
print()

# Mean of columns
tmp = []
for col in range(col):
    tmp.append(sum(mat[:,col])/row)
print(tmp)
print()

# Mean whole matrix
print(sum(sum(mat))/mat.size)