  
#Problem 38

#1) Is a number pandigital?

def is_pandigital(num):
    s = set(); num = str(num);
    if len(num) > 9: return False
    for i in num:
        s.add(i)
    if len(s) == 9 and "0" not in s:
        return True
    return False
 
def concatenate(num):
    prod = ""
    for i in range(1,10):
        prod += (str(i*num))
        if len(prod) >= 9: break
    return int(prod)

to_go = range(9,10) + range(91,99) + range(912,988) + range(9123,9877) + range(91234,98766)
max = 1
for i in to_go:
    temp = is_pandigital(concatenate(i))
    if temp and concatenate(i) > max:
        max = concatenate(i)
        print "The next max is", max
print "It's finished running.\nThe max is",max
