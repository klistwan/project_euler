#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.

dict = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40:5, 50: 5, 60: 5, 70: 7,  80:6, 90:6, 1000:11}

def getLength(num):
    if num in dict: return dict[num]
    elif num < 100: return getLength_twoDigits(num)
    elif not num % 100: return 7 + dict[num/100]
    else: return dict[num/100] + 10 + getLength_twoDigits(num%100) #10 is for "hundred and"

def getLength_twoDigits(num):
    if num in dict: return dict[num]
    else: return dict[num%10] + dict[10*(num/10)]

def main(max = 1000):
    return reduce(lambda k,y: k+y, [getLength(n) for n in xrange(1,max+1)], 0)
print main()
