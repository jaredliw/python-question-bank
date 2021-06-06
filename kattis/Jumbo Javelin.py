# CPU: 0.05 s
from sys import stdin
from functools import reduce

n = int(input())
print(reduce(lambda x, y: x + int(y), stdin.readlines(), 0) - n + 1)
