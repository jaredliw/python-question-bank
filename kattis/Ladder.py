# CPU: 0.05 s
from math import ceil, radians, sin

height, angle = map(int, input().split())
print(ceil(height / sin(radians(angle))))
