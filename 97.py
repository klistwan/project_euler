#Find the last 10 digits of the non-Mersenne prime which contains 2,357,207 digits: (2^843327830457)+1.

def main(a=2,b=7830457,c=28433,digits=10): return (c*pow(a,b,10**digits) + 1) % 10**digits

print main()
