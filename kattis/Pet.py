# CPU: 0.05 s
from sys import stdin

max_idx = 0
max_points = 0
for idx, line in enumerate(stdin, 1):
    cur = sum(map(int, line.split()))
    if cur > max_points:
        max_points = cur
        max_idx = idx
print(max_idx, max_points)
