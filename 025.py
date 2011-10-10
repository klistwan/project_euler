#What is the first term in the Fibonacci sequence to contain 1000 digits?

from math import ceil,log10,sqrt
def main(digits = 1000): return ceil((digits-1+log10(sqrt(5)))/log10((1+sqrt(5))/2))

print main()
    
        
