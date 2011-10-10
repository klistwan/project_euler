#Starting in the top left corner of a 22 grid, there are 6 routes 
#(without backtracking) to the bottom right corner.
#How many routes are there through a 2020 grid?

from useful import factorial
def main(a=20,b=20): return factorial(a+b)/(factorial(a)*factorial(b))

print main()
