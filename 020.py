#Find the sum of the digits in the number 100!
from useful import factorial

def main(n = 100): return reduce(lambda k,y: int(k)+int(y), str(factorial(n)),0)

print main()
