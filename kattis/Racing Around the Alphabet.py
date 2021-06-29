# CPU: 0.06 s
from math import pi

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
for _ in range(int(input())):
    aphorism = input()
    steps = 0
    for idx in range(1, len(aphorism)):
        last_idx = chars.index(aphorism[idx - 1])
        cur_idx = chars.index(aphorism[idx])
        if cur_idx < last_idx:
            last_idx, cur_idx = cur_idx, last_idx
        steps += min(cur_idx - last_idx, 28 - cur_idx + last_idx)
    print(steps * pi / 7 + len(aphorism))  # (pi * 60) / (28 * 15) = pi / 7
