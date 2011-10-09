#By considering the terms in the Fibonacci sequence whose values do not exceed 
#four million, find the sum of the even-valued terms.

import fibonacci
def main(max_n = 34):
    return sum(filter(lambda k: k%2==0, fibonacci.sequence(max_n)))

print main()
