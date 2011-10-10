max = 0
limit = 100

def digital_sum(n):
    n = str(int(n))
    l = []
    for i in n:
        l.append(int(i))
    return sum(l)

for a in range(1,limit):
    for b in range(1,limit):
        dsum = digital_sum(a ** b)
        if dsum > max: 
            max = dsum
            print a,b,"form",max,"as a result of",dsum
