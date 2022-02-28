n = int(input('Ange längd på kvadratisk matris: '))
M = [[1 if (j == i or i == n-j-1) else 0 for i in range(n)] for j in range(n)]
for i in M:
    print(i)