# CPU: 0.06 s
from functools import reduce

input()
print(-reduce(lambda x, y: x + int(y) if y[0] == "-" else x, input().split(), 0))
