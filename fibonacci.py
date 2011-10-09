"""Contains several algorithms for fibonacci calculations.
number(n): Returns the nth fibonacci number.
sequence(n): Returns the first n fibonacci numbers."""

def number(n):
    import time
    from math import sqrt
    root5 = sqrt(5)
    phi = 0.5 + root5/2
    return int(0.5 + phi**n/root5)

def sequence(n): return map(lambda k: number(k), xrange(1,n+1))

