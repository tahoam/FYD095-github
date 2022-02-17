def addMatrices(A, B):
    output = [[],[],[]]
    for i in range(len(A)):
        for j in range(len(A[1])):
            output[i].append(A[i][j]+B[i][j])

def substractMatrices(A, B):
    output = [[],[],[]]
    for i in range(len(A)):
        for j in range(len(A[1])):
            output[i].append(A[i][j]-B[i][j])

#mat1 = list(input('Input the first matrix: '))
#mat2 = list(input('Input the second matrix: '))
mat1 = list('[[1,1],[1,1]]')
mat2 = list('[[1,1],[2,3]]')
# Need to convert this list och chars to something of use!

if len(mat1) == len(mat2) and len(mat1[1]) == len(mat2[1]):
    cond = int(input('For addition type 1, all others are substraction.: '))
    if cond == 1:
        res = addMatrices(mat1, mat2)
    else:
        res = substractMatrices(mat1, mat2)
    print(res)
else:
    print('Yeet!')