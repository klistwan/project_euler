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
	
