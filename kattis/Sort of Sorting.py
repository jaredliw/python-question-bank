# CPU: 0.21 s
while True:
    n_lines = int(input())
    if n_lines == 0:
        break

    print(*sorted((input() for _ in range(n_lines)), key=lambda x: x[:2]), sep="\n")
    print()
