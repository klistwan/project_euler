#Using 042.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

def compute_score(name):
    """Returns score of a name, which is the sum of letters where A = 1, ..., Z = 26"""
    return sum(map(lambda k: ord(k)-64, list(name)))

def main(triangle_numbers = map(lambda n: 0.5*n*(n+1), xrange(1,21))):
    words = file("042.txt","r").read()[1:-1].split('","')
    scores = map(lambda n: compute_score(n), words)
    return len(filter(lambda k: k in triangle_numbers, scores))

print main()
