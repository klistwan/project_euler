def get_solutions(p):
    a = 1
    b = 2
    c = p - a - b
    sols = []
    while c - 2 >= a:
        to_go = range(b,((b+c)/2))
        if not to_go: #If it's empty, then goes here.
            ls = a*a + b*b
            rs = c*c
            if a*a + b*b == c*c:
                sols.append([a,b,c])
        else:
            for i in to_go: #Otherwise goes here.
                c = p - a - i
                if a*a + i*i == c*c:
                    sols.append([a,i,c])
        
        a += 1
        b += 1
        c = p - a - b
    return sols

max = 0
for i in range(12,1001):
    temp = len(get_solutions(i))
    if temp > max:
        max = temp
        print "New max is ", max, " thanks to perimeter of ", i
