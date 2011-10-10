from math import sqrt

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

primes = []
num = 2
for num in prime_sieve(100):
    for limit in range(540,560):
        while len(primes) != limit:
            if is_prime(num):
                primes.append(num)
            num += 1
        if is_prime(sum(primes)):
            if sum(primes) < 1000000: print sum(primes),"written by",len(primes)
            break
    primes = []

