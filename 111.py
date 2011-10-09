"""We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes. For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d)."""

import prime
from itertools import ifilter, permutations, repeat, izip

def M(n=10, d=None):
    return dict(izip(xrange(n), [8,9,8,9,9,9,9,9,8,9]))
    
def N(d,n=10):
    """For an n-digit prime, d is the digit that reappears."""
    primes,dict = [], M()
    if dict[d] == n-1:
        to_permute = list(repeat(str(d),n)) #['1','1','1','1']
        digits = [str(k) for k in range(10) if k!=d]
        current_permute = int("".join(to_permute))
        if prime.isprime(current_permute): primes.append(current_permute)
        for i in range(n):
            for digit in digits:
                to_permute[i] = digit
                cur_num = int("".join(to_permute))
                if prime.isprime(cur_num):
                    primes.append(cur_num)
            to_permute[i] = str(d)
        return len(primes)
    if dict[d] == n-2:
        to_permute = list(repeat(str(d),n)) #['1','1','1','1']
        digits = [str(k) for k in range(10) if k!=d]
        



    return 69

for i in range(0,10):
    print i,N(i)
#    break

