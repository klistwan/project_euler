##Problem 17
#dict = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40:5, 50: 5, 60: 5, 70: 7,  80:6, 90:6}

#def get_sum(end):
    #sum = 0
    #for i in range(1,end+1):
	#sum += get_length(i)
    #return sum

#def get_length(num):
    #if num==1000:
	#return 11
    #elif num<100:
	#return length_2_digits(num)
    #elif num % 100 == 0:
	#return 7 + dict[int(str(num)[0])]
    #else:
	#return dict[int(str(num)[0])] + 10 + length_2_digits(int(str(num)[1:]))

#def length_2_digits(num):
    #if 0 == int(str(num)[0]):
	#return dict[int(str(num)[1])]
    #elif num < 20 or num % 10 == 0:
	#return dict[num]
    #else:
	#first = int(str(num)[0])*10
	#second = int(str(num)[1])
	#return dict[first] + dict[second]
    
#print get_sum(1000)

      
###Problem 42
#f = file("words.txt","r")
#lines = f.readline()
#lines = lines[1:-1].split('","')

#def compute_score(name):
    #score = 0
    #for letter in name:
        #score += ord(letter)-64
    #return score

#list_of_scores = map(lambda n: compute_score(n), lines)

#list_of_triangle_nums = map(lambda n: 0.5 * n * (n + 1), range(1,21))
#print len(filter(lambda n: n in list_of_triangle_nums, list_of_scores))

##Problem 67
#f = file("triangle.txt","r")
##f = file("small_triangle.txt","r")
#lines = f.readlines()
#lines.reverse()
#new_tri = []
#for line in lines:
    #line = line.split()
    #line = map(lambda n: int(n), line)
    #new_tri.append(line)

#def row_into_sums(list_of_nums):
    #for i in range(len(list_of_nums)-1):
	#list_of_nums[i] = max(list_of_nums[i], list_of_nums[i+1])
    #return list_of_nums[:-1]

#def row_get_top_sums(list_of_nums, list_of_sums):
    #for i in range(len(list_of_nums)):
	#list_of_nums[i] = list_of_nums[i] + list_of_sums[i]
    #return list_of_nums

#def main_function():
    #for i in range(len(new_tri)-1):
	#new_tri[i] = row_into_sums(new_tri[i])
	#new_tri[i+1] = row_get_top_sums(new_tri[i+1], new_tri[i])
    #return new_tri[-1]
	
#print main_function()
	

##Problem 18
#f = file("smaller_triangle.txt","r")
##f = file("small_triangle.txt","r")
#lines = f.readlines()
#lines.reverse()
#new_tri = []
#for line in lines:
    #line = line.split()
    #line = map(lambda n: int(n), line)
    #new_tri.append(line)

#def row_into_sums(list_of_nums):
    #for i in range(len(list_of_nums)-1):
	#list_of_nums[i] = max(list_of_nums[i], list_of_nums[i+1])
    #return list_of_nums[:-1]

#def row_get_top_sums(list_of_nums, list_of_sums):
    #for i in range(len(list_of_nums)):
	#list_of_nums[i] = list_of_nums[i] + list_of_sums[i]
    #return list_of_nums

#def main_function():
    #for i in range(len(new_tri)-1):
	#new_tri[i] = row_into_sums(new_tri[i])
	#new_tri[i+1] = row_get_top_sums(new_tri[i+1], new_tri[i])
    #return new_tri[-1]
	
#print main_function()
	
#a = ""
#for i in range(1,1000000):
    #a += str(i)
#print a[1-1]
#print a[10-1]
#print a[100-1]
#print a[1000-1]
#print a[10000-1]
#print a[100000-1]
#print a[1000000-1]

#def num_in_top_bot(top,bot):
    #top_list = []
    #bot_list = []
    #top_list.append(int(str(top)[0]))
    #top_list.append(int(str(top)[1]))
    #bot_list.append(int(str(bot)[0]))
    #bot_list.append(int(str(bot)[1]))
    #for i in top_list:
	#if i in bot_list and i!=0:
	    #bot_list.remove(i)
	    #top_list.remove(i)
	    #if bot_list[0] != 0:
		#return float(top_list[0]) / bot_list[0]
    #return 1

#for top in range(10,100):
    #for bot in range(10,100):
	#if top != bot and num_in_top_bot(top,bot) == float(top)/bot and float(top)/bot < 1:
	    #print float(top)/bot, " comes from ", top, "/", bot
	    
import itertools
a = list(itertools.permutations([1,2,3,4,5,6,7,8,9,0],4))
list_combs = []
for i in a:
    list_combs.append(list(i))
list_of_combs = []
for list in list_combs:
    new_list = ''
    for ele in list:
	new_list += str(ele)
    list_of_combs.append(int(new_list))
list_of_combs = filter(lambda (n): len(str(n))==4, list_of_combs)
#print list_of_combs
#for i in list_of_combs:
 #   a = list(itertools.permutations([i]))
  #  pass
  
def is_prime(n):
    if n in prime_sieve(n+1):
	return True
    return False

from math import sqrt

def prime_sieve(limit):
    lop = []
    cur_num = 2
    l2g = range(2,limit)
    while cur_num < sqrt(limit):
	lop.append(cur_num)
	l2g = filter(lambda n: n%cur_num != 0, l2g)
	cur_num = l2g[1]
    lop.extend(l2g)
    return lop
  
##Problem 31
#target = 200
#coins = [1,2,5,10,20,50,100,200]
#ways = [1]+[0]*target

#for coin in coins:
    #for i in range(coin, target+1):
	#ways[i] += ways[i-coin]
#print "Answer to Problem 31 is", ways[target]
  
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
