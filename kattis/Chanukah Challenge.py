# CPU: 0.15 s
for _ in range(int(input())):
    day, n = map(int, input().split())
    print(day, n + n * (n + 1) // 2)