def is_prime(n):
    from math import sqrt
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
                    
def get_prime_factors(n):
    factor, factors = 2, set()
    if is_prime(n):
        temp = set()
        temp.add(n)
        return temp
    while n != 1:
        if n % factor != 0: factor += 1
        else: 
            factors.add(factor)
            n = n/factor
    return factors

cur_num = 130000
consec = 1
while consec != 2:
    l = range(cur_num,cur_num+4)
    l2 = range(cur_num,cur_num+2)
    if map(lambda n: len(get_prime_factors(n)), l2) == [4,4]:
        if map(lambda n: len(get_prime_factors(n)), l) == [4,4,4,4]:
            consec = 2
            print l
    cur_num += 1
    if cur_num % 500 == 0: print "Currently at",cur_num


            
