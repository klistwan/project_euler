#Which starting number, under one million, produces the longest chain?
#The following iterative sequence is defined for the set of positive integers:

#n/2 (n is even)
#3n + 1 (n is odd)

chains = {1: 1}
def CollatzChain(n):
    if not n in chains: 
        if n%2: chains[n] = CollatzChain(3*n+1) + 1
        else: chains[n] = CollatzChain(n/2) + 1
    return chains[n]

def main(max_n = pow(10,6)):
    cur_max = (0,0)
    for num in range(3,max_n,2): 
        current_chain = CollatzChain(num)
        if current_chain > cur_max[1]: cur_max = (num,current_chain)
    return cur_max[0]

print main()
