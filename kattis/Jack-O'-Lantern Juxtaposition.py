# CPU: 0.06 s
from functools import reduce

print(reduce(lambda x, y: x * int(y), input().split(), 1))
