# CPU: 0.14 s
for _ in range(int(input())):
    test_case, num = map(int, input().split())
    print(test_case,
          int(num / 2 * (1 + num)),  # S_n = n / 2 * (a + l)
          int(num ** 2),  # S_n = n / 2 * [2a + (n-1)d]
          int(num ** 2 + num))  # S_n = n / 2 * [2a + (n-1)d]
