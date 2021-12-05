# CPU: 0.16 s
while True:
    n_lines = int(input())
    if n_lines == 0:
        break

    l1 = list(map(int, (input() for _ in range(n_lines))))
    sorted_l1 = sorted(l1)
    order = [sorted_l1.index(key) for key in l1]

    l2 = map(int, (input() for _ in range(n_lines)))
    for _, item in sorted(enumerate(sorted(l2)), key=lambda x: order.index(x[0])):
        print(item)
    print()
