#What is the value of the first triangle number to have over 500 divisors?

import prime
def triangle(n): return n*(n+1)/2
def num_of_divisors(num): return reduce(lambda k,y: k*y, [k+1 for k in prime.factorization(num).values()])

def main(index = 100):
    while 1:
        current = triangle(index)
        current_divisors = num_of_divisors(current)
        if current_divisors > 500: return current
        index += 1

print main()
