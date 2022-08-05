# CPU: 0.06 s
import sys
from collections import Counter
from math import factorial

for line in sys.stdin.readlines():
    line = line.rstrip()
    c = Counter(line)
    ans = factorial(len(line))
    for val in c.values():
        ans //= factorial(val)
    print(ans)
