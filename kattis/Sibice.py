# CPU: 0.06 s
from math import hypot

n, width, height = list(map(int, input().split()))
longest = hypot(width, height)
for _ in range(n):
    print('DA' if int(input()) <= longest else 'NE')
