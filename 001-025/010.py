#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import prime
def main(max_n = 2*pow(10,6)-1): return sum(prime.sieve(max_n))

print main()
