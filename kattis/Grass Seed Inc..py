# CPU: 0.06 s
from functools import reduce
from sys import stdin

cost = float(input())
input()
print(reduce(lambda x, y: x + float(y.split()[0]) * float(y.split()[1]) * cost, stdin.readlines(), 0))
