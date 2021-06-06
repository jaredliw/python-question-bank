# CPU: 0.02 s
from sys import stdin

print(len(list(filter(lambda x: x < 0, map(int, stdin.readlines()[1].split())))))
