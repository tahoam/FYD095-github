# Sieve of Eratosthenes
def getPrimes(n):
    sieve = [True] * n
    for i in range(2, int(n**(0.5) + 1)):
        if sieve[i] == True:
            for j in range(i**2, n, i):
                sieve[j] = False
    return  [i for i in range(2, n) if sieve[i]]

def isPrime(primes, inp):
    # The sieve dosn't calculate primes below 2.
    if inp == 1:
        return True
    for prime in primes:
        if inp == prime:
            return True
    return False


input_number = int(input('Ange ett positivt heltal! '))

primes_list = getPrimes(input_number + 1)

print(isPrime(primes_list, input_number))