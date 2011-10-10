from time import sleep, time
a = time()
def get_poly(type,n):
    if type == "tri":
        return n*(n+1)/2
    if type == "sqr":
        return n*n
    if type == "pent":
        return n*(3*n-1)/2
    if type == "hex":
        return n*(2*n-1)
    if type == "hept":
        return n*(5*n-3)/2
    if type == "oct":
        return n*(3*n-2)

tris = map(lambda n: get_poly("tri",n), range(45,141))
sqrs = map(lambda n: get_poly("sqr",n), range(32,100))
pents = map(lambda n: get_poly("pent",n), range(26,82))
hexs = map(lambda n: get_poly("hex",n), range(23,71))
hepts = map(lambda n: get_poly("hept",n), range(21,64))
octs = map(lambda n: get_poly("oct",n), range(19,59))

for i in tris:
    print "\n"
    print filter(lambda n: str(n)[2:] == str(i)[:2], sqrs), i, filter(lambda n: str(n)[:2] == str(i)[2:], sqrs),"sqrs"
    print filter(lambda n: str(n)[2:] == str(i)[:2], pents), i, filter(lambda n: str(n)[:2] == str(i)[2:], pents),"pents"
    print filter(lambda n: str(n)[2:] == str(i)[:2], hexs), i, filter(lambda n: str(n)[:2] == str(i)[2:], hexs),"hexs"
    print filter(lambda n: str(n)[2:] == str(i)[:2], hepts), i, filter(lambda n: str(n)[:2] == str(i)[2:], hepts),"hepts"
    print filter(lambda n: str(n)[2:] == str(i)[:2], octs), i, filter(lambda n: str(n)[:2] == str(i)[2:], octs),"octs"

    
print len(octs)
b = time()
print b-a
