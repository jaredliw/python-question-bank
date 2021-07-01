# CPU: 0.06 s
test_case = 1
while True:
    names = [input() for _ in range(int(input()))]
    if not names:
        break
    print("SET", test_case)
    print(*names[::2], *names[1::2][::-1], sep="\n")
    test_case += 1
