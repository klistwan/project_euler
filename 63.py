from math import pow
from time import time, sleep

a = time()

def get_powers(power):
    num = 1
    l = []
    while 1:
        temp = len(str(int(pow(num,power))))
        if temp == power:
            l.append(num)
        num += 1
        if temp > power: break
    return l
sum = 0
for i in range(1,50):
    sum += len(filter(lambda n: n<10, get_powers(i)))
print sum









b = time()
print "It took:",b-a
