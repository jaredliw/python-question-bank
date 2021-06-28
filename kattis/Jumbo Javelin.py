# CPU: 0.05 s
from functools import reduce
from sys import stdin

n = int(input())
print(reduce(lambda x, y: x + int(y), stdin.readlines(), 0) - n + 1)
