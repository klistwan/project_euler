#How many numbers below a googol (10^100) are not bouncy?
def binomial(n, k):
  nt = 1
  for t in range(min(k, n-k)):
    nt = nt*(n-t)//(t+1)
  return nt

n=100
print binomial(n+10,10) + binomial(n+9,9) - 10*n - 2
