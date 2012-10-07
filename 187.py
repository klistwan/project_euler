"""A composite is a number containing at least two prime factors. For example, 15 = 3  5; 9 = 3  3; 12 = 2  2  3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n  108, have precisely two, not necessarily distinct, prime factors?"""

import itertools
import prime
from math import sqrt

if __name__ == '__main__':
  limit = pow(10,8)
  count = 0
  primes = prime.sieve(limit)
  for i in xrange(len(primes)):
    for j in xrange(i, len(primes)):
      if primes[i] * primes[j] >= limit:
        break
      count += 1
  print count
