# CPU: 0.05 s
from functools import reduce

print(reduce(lambda x, y: x + int(y), input().split(), 0))
