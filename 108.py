
from time import time
 
print "#108 - Diophantine Equation: What is the least value of n for which\n\
the number of distinct solutions exceeds one-thousand?\n"
 
start = time()
result = 0
 
def main(e):
    n = 30
    while True:
        c = 0
        for x in xrange(n+1,n*2+1):
            y = float(-n*x)/(n-x)
            if y % 1 == 0 and y > 0:
                c += 1
        if c > e:                 
            return n
        if n % 10000 == 0: print n
        n += 30
 
result = main(1000)
 
 
print "Answer:", result
print "\ndone in", str(time()-start), "Seconds"
print "any key to continue..."
getch()
