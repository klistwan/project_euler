from itertools import permutations
from math import pow
from time import sleep,time

s = time()
def is_cube(x):
    x, y,y1 = int(x), None,2
    while y != y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d/2)/d
    if y*y*y != x: return False
    return True

cur_num = 450
dict = {1:[[0],0]} #Needs to be non-empty

while max(map(lambda k: k[1], dict.values())) < 5:
    cur_num += 1
    asc_num = int(''.join(sorted(list(str(int(pow(cur_num,3)))), reverse=True)))
    if asc_num in dict: 
        dict[asc_num][0] = dict[asc_num][0] + [cur_num]
        dict[asc_num][1] += 1 #Increases count
    else: dict[asc_num] = [[cur_num],1]
    if cur_num % 1000 == 0: print "At:",cur_num
    
print min(filter(lambda q: q[1]==5,dict.values())[0][0])
t = time()
print "It took:",t-s
