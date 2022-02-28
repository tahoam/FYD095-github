def geometricSeries(a1, q, n, i=0):
    if n <= 0:
        an = a1 * q ** (i-1) 
        print(an)
        return


    geometricSeries(a1, q, n-1, i+1)

start = int(input('a: '))
factor = int(input('q: '))
num = int(input('n: '))

geometricSeries(start, factor, num)