#Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468. Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

#We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

#Find the least number for which the proportion of bouncy numbers is exactly 99%.

def isBouncy(n):
    """Returns True if n is a bouncy number; False otherwise."""
    inc, dec = 0,0
    num_list = [int(a) for a in str(n)]
    for index in range(0,len(num_list)-1):
        if num_list[index] > num_list[index+1]: dec = 1
        if num_list[index] < num_list[index+1]: inc = 1
    if inc and dec: return True
    return False

def main():
    bouncyNumbers = 0
    current_number = 1
    
    while (bouncyNumbers*100 != current_number*99):
        current_number += 1
        if isBouncy(current_number): bouncyNumbers += 1
    return current_number
        
print main()
