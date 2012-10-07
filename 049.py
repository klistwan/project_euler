'''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

What 12-digit number do you form by concatenating the three terms in this sequence?'''

import prime
import itertools
import pdb

def generate_primes():
  return filter(lambda k: k > 999, prime.sieve(10000))

primes = generate_primes()

def possible_combinations(number):
  return list(set(filter(lambda k: k in primes, map(lambda k: int("".join(k)), set(itertools.permutations(list(str(number))))))))

def find_pair():
  verified = [1487, 4817, 8147]
  for number in primes:
    if number in verified:
      continue

    print "\nCurrently investigating: %d\n" % number

    combinations = possible_combinations(number)
    verified += combinations

    if len(combinations) < 3:
      continue

    differences = {}
    pairs = itertools.combinations(combinations, 2)
    for pair in pairs:
      
      difference = max(pair) - min(pair)
      if difference in differences.keys():
        for i in pair:
          if i in differences[difference]:
            print pair
            pdb.set_trace()
            break
      else:
        differences[difference] = pair

find_pair()
