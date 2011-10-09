#Find the greatest product of five consecutive digits in the 1000-digit number.
#Number is located in 008.txt

def main():
    number = "".join([line.strip() for line in file("008.txt","r").readlines()])
    max_product = 0
    for i in range(len(number)-5):
        temp = number[i:i+5]
        current_product = reduce(lambda k,y: int(k)*int(y), temp, 1)
        if current_product > max_product: max_product = current_product
    return max_product

print main()
