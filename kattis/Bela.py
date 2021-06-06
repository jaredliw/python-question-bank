# CPU: 0.06 s
n, dominant_suit = input().split()
rules = {"A": (11, 11), "K": (4, 4), "Q": (3, 3), "J": (20, 2), "T": (10, 10), "9": (14, 0), "8": (0, 0), "7": (0, 0)}
points = 0
for _ in range(4 * int(n)):
    inp = input()
    points += rules[inp[0]][inp[1] != dominant_suit]
print(points)
