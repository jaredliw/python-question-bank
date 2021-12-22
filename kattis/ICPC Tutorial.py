# CPU: 0.05 s
from math import log2

def factorial(num):
    precomputed = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600]
    if num > 12:
        return float("inf")  # TLE, don't compute
    else:
        return precomputed[num]

m, n, t = map(int, input().split())
if t == 1:
    n = factorial(n)
elif t == 2:
    n = pow(2, n)
elif t == 3:
    n = pow(n, 4)
elif t == 4:
    n = pow(n, 3)
elif t == 5:
    n = pow(n, 2)
elif t == 6:
    n *= log2(n)
print("AC" if n <= m else "TLE")
