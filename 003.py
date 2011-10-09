#What is the largest prime factor of the number 600851475143

import prime
def main(n = 600851475143):
    return max(prime.factorization(n).keys())

print main()
