def get_pents(limit):
    lopents = []
    for n in range(1,limit):
        lopents.append(n*(3*n-1)/2)
    return lopents

from math import sqrt
def is_pent(n):
    a = (1 + sqrt(1+24*n))/6
    b = (1 - sqrt(1+24*n))/6
    checka = int(a) == a
    checkb = int(b) == b
    if a>0 and b<0:
        return checka
    elif a<0 and b>0:
        return checkb
    else:
        return checka or checkb

rng = get_pents(10000)
for a in rng:
    for b in filter(lambda n: n>a, rng):
       if is_pent(a+b) and is_pent(b-a):
           print a,b,"both their sum",a+b,"and their diff",b-a,"are pent"
#       if is_pent(a+b):
 #          print a,b,"only their sum is pent:",a+b
  #     if is_pent(b-a):
   #        print a,b,"only their diff is pent:",b-a

