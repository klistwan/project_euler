#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return n == int(str(n)[::-1])

def main(cur_max = 0):
    for i in xrange(100,1000):
        for j in xrange(100,1000):
            cur_num = i*j
            if is_palindrome(cur_num): 
                if cur_num > cur_max: cur_max  = cur_num
    return cur_max

print main()
