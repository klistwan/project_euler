from math import sqrt, pow

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
                    
def topR(n):
    return 4*pow(n,2) - 10*n + 7

def topL(n):
    return 4*pow(n,2) - 8*n + 5

def botL(n):
    return 4*pow(n,2) - 6*n + 3

def botR(n):
    return 4*pow(n,2) - 4*n + 1

#26410 is too high. 26375 is too low

def solution(cur_num):
    f = open('61.txt','w')
    cur_num = 3
    n = 2 + cur_num/2 #1252
    topRL = map(lambda m: topR(m), range(2,n))#from 2 to 1251
    topLL = map(lambda m: topL(m), range(2,n))
    botRL = map(lambda m: botR(m), range(2,n))
    botLL = map(lambda m: botL(m), range(2,n))
    total = topRL + topLL + botRL + botLL + [1]
    primes = filter(lambda k: is_prime(k), total)
    prcnt = len(primes)/float(len(total))
    print "Currently at:",cur_num,"% of primes is:",prcnt
    f.write(','.join([str(cur_num),str(prcnt)+"\n"]))

    while prcnt > 0.10:
        cur_num += 2
        n = 2 + cur_num/2
        new_total = [topR(n),topL(n),botR(n),botL(n)]
        new_primes = filter(lambda k: is_prime(k), new_total)
        total += new_total
        primes += new_primes
        prcnt = len(primes)/float(len(total))
        print "Currently at:",cur_num,"% of primes is:",prcnt
        f.write(','.join([str(cur_num),str(prcnt)+"\n"]))

    f.close()
solution(2501)
