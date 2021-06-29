# CPU: 0.07 s
n = int(input())
last = input()
score = 0
for _ in range(n - 1):
    cur = input()
    if cur == last:
        score += 1
    last = cur
print(score)
