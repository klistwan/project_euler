

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
	  
