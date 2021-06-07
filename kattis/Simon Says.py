# CPU: 0.06 s
from sys import stdin

print("".join(map(lambda x: x[10:] if x.startswith("Simon says") else "", stdin.readlines())))