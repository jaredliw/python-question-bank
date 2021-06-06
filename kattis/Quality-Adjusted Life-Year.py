from sys import stdin
from functools import reduce

input()
print(reduce(lambda x, line: x + float(line.split()[0]) * float(line.split()[1]), stdin.readlines(), 0))
