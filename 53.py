def factorial1(n):
    prod = 1
    if n == 0: return 1
    if n == 1: return 1
    prod = n * factorial1(n-1)
    return prod

total = 0
for n in range(1,101):
    for r in range(1,n):
        value = factorial1(n) / (factorial1(r) * factorial1(n-r))
        if value > 1000000: 
            total += 1
print total
