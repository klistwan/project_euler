from math import sqrt
from itertools import combinations, permutations

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r, f = int(sqrt(n)), 5
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

def concatenable_primes(n1,n2):
    if is_prime(int(str(n1)+str(n2))):
        return is_prime(int(str(n2)+str(n1)))
    return False

def get_concatenable_to_(num):
    l = []
    for n in filter(lambda n: n>num, prime_sieve(100000)):
        if concatenable_primes(num,n): l.append(n)
    return l

l_to_3 = get_concatenable_to_(13)
l_to_7 = get_concatenable_to_(5197)
intersect = list(set(l_to_3) & set(l_to_7)) + [13,5197]

def has_property(lon):
    for pair in permutations(lon,2):
        check = int(str(pair[0]) + str(pair[1]))
        if not is_prime(check): return False
    print sum(lon)
    return True

for i in combinations(intersect,5):
    print "currently at",i
    if has_property(list(i)):
        print "THIS IS THE ONE",list(i)
        break

