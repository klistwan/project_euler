from math import sqrt
from time import time
a = time()
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f<= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f += 6
    return True
                    
def prime_sieve(limit):
    primes = []
    cur_num = 2
    remaining = range(2,limit)
    while cur_num <= sqrt(limit):
	primes.append(cur_num)
	remaining = filter(lambda n: n%cur_num != 0, remaining)
	cur_num = remaining[0]
    primes.extend(remaining) #Adds the rest of the primes into the list
    return primes

def find_relative_primes(n):
    if is_prime(n): return range(1,n)
    return filter(lambda k: is_relative_prime(n,k), range(1,n))
    
def is_relative_prime(a,b):
    if set(get_factors(a)).intersection(set(get_factors(b))): return False
    return True

def get_factors(n):
    if is_prime(n): return [n]
    divisor = 2
    lst = [n]
    for prime in prime_sieve(n):
        if n % prime == 0:
            lst.append(prime)
            n = n / prime
        if n == 1: break
    return list(set(lst))

def phi_function(n):
    return len(find_relative_primes(n))

def n_by_phi_function(n):
    return float(n)/phi_function(n)


