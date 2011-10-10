def l(n):
    return map(lambda k: int(k), list(str(n)))

def sum_of_digs(n):
    return sum(map(lambda k: k*k, l(n)))

def find_end(n):
    while sum_of_digs(n) not in [1,89]:
        n = sum_of_digs(n)
        
    if sum_of_digs(n) == 1: return 1
    return 89
from time import time

num = 1
total = 0
a = time()
while num < 10000000:
    if find_end(num) == 89: total += 1
    if num % 10000 == 0:
        b = time()
        print "Currently at:",num,"took:",b-a
        a = time()
        print num
    num += 1

print total
