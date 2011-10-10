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

def disprove_goldbach(limit):
    cur_num = 25
    while cur_num < limit:
        if cur_num % 1001 == 0: print "Currently at",cur_num
        solns = 0
        if not is_prime(cur_num):
            for prime in prime_sieve(cur_num):
                check = sqrt((cur_num - prime)/2)
                if check == int(check):
                    solns = 1
                    break
            if solns != 1: print cur_num,"DISPROVES THE GOLDBACH CONJECTURE**"
        cur_num += 2

disprove_goldbach(10000)
