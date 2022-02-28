from operator import truediv


def unknownInput(*args):
    cond = True
    for i in args:
        try:
            int(i)
        except ValueError:
            cond = False
    if cond:
        sum =0
        for i in args:
            sum = sum + i**2
        return sum
    else:
        return 'Input was not only digits.'

s = unknownInput(1,2,3,4,5,6,7,8,9,10, 'hej')
print(s)