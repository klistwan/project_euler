def is_0_to_9_pandigital(n):
    n = str(n)
    if len(str(n)) != 10: return False
    for i in range(0,10):
        i = str(i)
        if len(i + n.replace(i,'')) == len(n):
            n = n.replace(i,'')
        else: return False
    return True

def has_special(n):
    if not is_0_to_9_pandigital(n): return False
    n = str(n)
    rng = [2,3,5,7,11,13,17]
    for i in range(7):
        if int(n[i+1:i+4]) % rng[i] != 0: return False
    return True

def d3(divisor):
    lop = []
    start = divisor
    while start < 1000:
        a = set()
        if len(str(start)) == 2:
            lop.append(start)
        else: 
            for i in str(start):
                a.add(i)
            if len(a) == 3:
                lop.append(start)
        start += divisor
    return lop


l17 = d3(17)
l13 = d3(13)
l11 = d3(11)
d7 = d3(7)

for h in l11:
    h = str(h)
    if len(h) == 3:
        hcheck = h[1:3]
        for i in l13:
            i = str(i)
            if hcheck == i[:2]:
                if len(i) == 3:
                    icheck = i[1:3]
                    for m in l17:
                        m = str(m)
                        if icheck == m[:2]:
                            print h,i,m


import itertools
import time

def get_divisibles(s):
    """Get the 7 divisibles"""
    x = list(str(s))
    L = []
    for i in xrange(1, 8):
        d = x[i] + x[i + 1] + x[i + 2]
        L.append(d)
    return L

def isdivisible(y, LL):
    """Check the 7 divisibles"""
    if int(y[0]) % int(LL[0]) == 0 and int(y[1]) % int(LL[1]) == 0 \
       and int(y[2]) % int(LL[2]) == 0 and int(y[3]) % int(LL[3]) == 0 \
       and int(y[4]) % int(LL[4]) == 0 and int(y[5]) % int(LL[5]) == 0 \
       and int(y[6]) % int(LL[6]) == 0:
        return True
    else:
        return False

def main():
    """Main Program"""
    start_time = time.time()
    summer = 0
    x = itertools.permutations('0123456789', 10)
    for n in x:
        s = ''.join(n)
        y = get_divisibles(s)
        LL = [2, 3, 5, 7, 11, 13, 17]
        z = isdivisible(y, LL)
        if z == True:
            summer = summer + int(s)
        else:
            continue
    print "Answer = ", summer
    stop_time = time.time()
    run_time = stop_time - start_time
    print "run_time = ", run_time

main()
