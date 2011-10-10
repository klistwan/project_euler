#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import prime

def main(factors = {}):
    for num in xrange(11,21):
        current_factors = prime.factorization(num)
        print "Currently we have:", factors
        print num,"has the factors:",current_factors
        for key in current_factors.keys():
            if key not in factors: factors[key] = current_factors[key]
            elif factors[key] < current_factors[key]: factors[key] = current_factors[key]
    results = [a**b for a,b in zip(factors.keys(), factors.values())]
    return reduce(lambda k,x: k*x, results, 1)

print main()
