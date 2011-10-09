#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers, in the file "013.txt"
def main():
    f = file("013.txt","r")
    return str(sum(map(lambda line: int(line), f.readlines())))[:10]

print main()

