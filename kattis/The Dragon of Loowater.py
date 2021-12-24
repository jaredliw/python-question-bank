# CPU: 0.38 s
while True:
    n_heads, n_knights = map(int, input().split())
    if n_heads == n_knights == 0:
        break

    heads = sorted((int(input()) for _ in range(n_heads)))
    knights = sorted((int(input()) for _ in range(n_knights)))

    head_ptr = 0
    knight_ptr = 0
    cost = 0
    while head_ptr < n_heads and knight_ptr < n_knights:
        if heads[head_ptr] <= knights[knight_ptr]:
            cost += knights[knight_ptr]
            head_ptr += 1
        knight_ptr += 1

    if head_ptr < n_heads:
        print("Loowater is doomed!")
    else:
        print(cost)
