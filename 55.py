def reverse(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    if n == reverse(n): return True
    return False

def is_lychrel(n):
    count = 0
    while count < 50:
        n += reverse(n)
        if is_palindrome(n): 
            count += 1
            return False
        count += 1
    return True

rng = range(1,10000)
print len(filter(lambda num: is_lychrel(num), rng))
