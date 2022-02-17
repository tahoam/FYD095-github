n = input_str = int(input('Enter the number of points: '))
a = input_str = int(input('Enter the staring point: '))
b = input_str = int(input('Enter the end point: '))

diff = b - a
step = diff/(n-1)
output = []
for i in range(n):
    output.append(a + step*i)

print(output)