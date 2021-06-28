# CPU: 0.05 s
for _ in range(int(input())):
    n, *outlets = list(map(int, input().split()))
    print(sum(outlets) - n + 1)
