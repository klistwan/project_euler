#What is the total of all the name scores in the file, 022.txt?

def compute_score(name):
    """Calculuates the score of a name, where A = 1, ... Z = 26"""
    return sum(map(lambda k: ord(k)-64, list(name)))
    
def main():
    names = sorted(file("022.txt","r").read()[1:-1].split('","'))
    name_scores = map(lambda k: compute_score(k), names)
    return sum(map(lambda k: k[0]*k[1], zip(xrange(1,len(names)+1), name_scores)))

print main()
