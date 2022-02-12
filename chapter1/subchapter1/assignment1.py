print('Insert coefficients for the quadratic function ax^2+bx+c:')
print('a=')
a = int(input())

print('b=')
b = int(input())

print('c=')
c = int(input())

pos_root = - b/2 + ((b/2)**2 - c)**(1/2)
neg_root = - b/2 - ((b/2)**2 - c)**(1/2)

print(f'The roots are {neg_root} and {pos_root}!')