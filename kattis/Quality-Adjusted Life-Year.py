# CPU: 0.06 s
# from sys import stdin
# from functools import reduce
#
# input()
# print(reduce(lambda x, line: x + float(line.split()[0]) * float(line.split()[1]), stdin.readlines(), 0))

# CPU: 0.02 s
from sys import stdin

print(eval(''.join(stdin.readlines()[1:]).replace('\n', '+').replace(' ', '*')[:-1]))
