#Find the difference between the sum of the squares of the first one hundred 
#natural numbers and the square of the sum.

def main(nums = xrange(1,101)):
    return pow(sum(nums),2)- sum(map(lambda k: k*k, nums))

print main()
