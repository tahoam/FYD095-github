print('Insert coefficients for the quadratic function ax^2+bx+c:')
print('a=')
a = int(input())

print('b=')
b = int(input())

print('c=')
c = int(input())

# a = 0 ok, since we assume two roots. Can't be a linear function.
pos_root = (- b + (b**2 - 4*a*c)**(1/2)) / (2*a)
neg_root = (- b - (b**2 - 4*a*c)**(1/2)) / (2*a)

print(f'The roots are {neg_root} and {pos_root}!')