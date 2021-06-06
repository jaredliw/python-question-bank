# runtime: 0.06 s
from sys import stdin
from functools import reduce

cost = float(input())
input()
print(reduce(lambda x, y: x + float(y.split()[0]) * float(y.split()[1]) * cost, stdin.readlines(), 0))
