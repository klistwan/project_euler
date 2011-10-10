
a = 2
b = 7830457
c = 28433
m = 10 #Number of ending digits we want.
print (c * pow(a,b,10**m) + 1) % 10**m
