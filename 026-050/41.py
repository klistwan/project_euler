def is_prime(n):
    if n in prime_sieve(n+1):
	return True
    return False

from math import sqrt

def prime_sieve(limit):
    lop = []
    cur_num = 2
    l2g = range(2,limit)
    while cur_num < sqrt(limit):
	lop.append(cur_num)
	l2g = filter(lambda n: n%cur_num != 0, l2g)
	cur_num = l2g[1]
    lop.extend(l2g)
    return lop

def n_pandigital(n):
    n_digit = 0
    num = str(n)
    while num != "":
        n_digit += 1
        if len(num.replace(str(n_digit),'') + str(n_digit)) == len(num):
            num = num.replace(str(n_digit),'')
        else: return 0
    return n_digit
        
for i in prime_sieve(10000000):
    if n_pandigital(i) > 0:
        print i, "is", n_pandigital(i), "-pandigital"


