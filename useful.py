from math import log10

def factorial(n): return reduce(lambda k,y: k*y, xrange(2,n+1), 1)


#To compute the number of digits in a number:
def find_digits(n):
    return int(log10(n)) + 1

#print find_digits(2482),"is equal to 4... unless I did it wrong"

#To compute the last K digits in a number
#We just have to do % 10**K

def get_last_k_digits(n,k):
    return n % 10**k

#print get_last_k_digits(421842,3),"should be 842... unless I did it wrong"
