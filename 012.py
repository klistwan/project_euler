#What is the value of the first triangle number to have over five hundred divisors?

import prime
def triangle(num): return 0.5*(pow(num,2)+num)

def num_of_divisors(num): 
    return reduce(lambda k,y: k*y, [k+1 for k in prime.factorization(num).values()])

triangles = map(lambda k: triangle(k), range(2,10))
print triangles

max_n = 0
i = 1
while max_n < 520:
    i+=1
    temp = num_of_divisors(triangle(i))
    if temp > max_n: max_n = temp
    print "currently on:",triangle(i),max_n
