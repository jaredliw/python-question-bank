# CPU: 0.06 s
from math import cos, radians, sin

for _ in range(int(input())):
    v0, theta, x, h1, h2 = map(float, input().split())
    t = x / (v0 * cos(radians(theta)))
    print("Safe" if h1 + 1 <= v0 * t * sin(radians(theta)) - 4.905 * t ** 2 <= h2 - 1 else "Not Safe")
