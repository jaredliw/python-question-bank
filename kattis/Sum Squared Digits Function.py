# CPU: 0.09 s
for _ in range(int(input())):
    test_case, base, num = map(int, input().split())
    ans = 0
    while num != 0:
        ans += (num % base) ** 2
        num //= base
    print(test_case, ans)
