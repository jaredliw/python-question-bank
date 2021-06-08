# CPU: 0.10 s
from math import pi

while True:
    radius, total, in_circle = map(float, input().split())
    if radius == 0:
        break
    else:
        print(pi * radius ** 2, (2 * radius) ** 2 * in_circle / total)
