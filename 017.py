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
