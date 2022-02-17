# Sieve of Eratosthenes
def getPrimes(n):
    sieve = [True] * n
    for i in range(2, int(n**(0.5) + 1)):
        if sieve[i] == True:
            for j in range(i**2, n, i):
                sieve[j] = False
    return  [i for i in range(2, n) if sieve[i]]

input_number = int(input('Ange ett positivt heltal! '))

primes = getPrimes(input_number)
factors = []

for i in primes:
    while input_number % i == 0:
        input_number /= i
        factors.append(i)

print(factors)