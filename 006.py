def main(nums = xrange(1,101)):
    return pow(sum(nums),2)- sum(map(lambda k: k*k, nums))

print main()
