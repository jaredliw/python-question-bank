# CPU: 0.05 s
from sys import stdin

print(len(set(map(lambda x: int(x) % 42, stdin.readlines()))))
