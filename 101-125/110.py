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

primes = filter(lambda k: is_prime(k), xrange(2,51))
 
mult = lambda x: reduce(lambda y, z: y * z, x, 1)
 
translate = lambda x: mult(primes[i] ** ((x[i] - 1) // 2) for i in range(len(x)))
 
def generator(limit):
    l = [1] * 14
    while l[13] < limit:
        i = 13
        while i > 0 and (l[i] == l[i-1]):
            l[i] = 1
            i -= 1
        l[i] += 2
        yield l
 
if __name__ == '__main__':
    result = min(translate(l) for l in generator(13) if mult(l) > 4000000)
    print("The result is:", result)
