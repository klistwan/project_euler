#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Rewrote Ruby implementation of the solution from http://projecteuler.net/thread=9
def main(sum = 1000, m = 0):
    from math import sqrt
    for n in xrange(sum+1):
        delta = n**2 + 2*sum
        m1 = (-n + sqrt(delta))/2.0
        m2 = (-n - sqrt(delta))/2.0
        if int(m1) == m1 and m1 > n: m = m1
        elif int(m2) == m2 and m2 > n: m = n2
        if m != 0: return reduce(lambda a,b: a*b, [2*m*n, m**2 - n**2, m**2 + n**2], 1)

print main()
