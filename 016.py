#What is the sum of the digits of the number 2^1000?

def main(n = 1000): return sum([int(k) for k in str(2**n)])
print main()
