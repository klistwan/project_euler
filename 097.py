#Find the last 10 digits of the non-Mersenne prime which contains 2,357,207 digits: (2^843327830457)+1.

def main(coefficient=28433, power=7830457,last_n_digits=10): 
    return (coefficient*pow(2,power,10**last_n_digits) + 1) % 10**last_n_digits

print main()
