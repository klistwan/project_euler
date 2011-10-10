#Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    return sum(set(range(3,1000,3)).union(set(range(5,996,5))))

print main()
