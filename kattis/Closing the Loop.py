# CPU: 0.07 s
for tc in range(1, int(input()) + 1):
    input()
    blue = []
    red = []
    for rope in input().split():
        length, color = rope[:-1], rope[-1]
        length = int(length)
        if color == "B":
            blue.append(length)
        else:
            red.append(length)
    blue.sort(reverse=True)
    red.sort(reverse=True)

    total_length = 0
    for rope1, rope2 in zip(blue, red):
        total_length += rope1
        total_length += rope2
        total_length -= 2  # 2 knots
    print(f"Case #{tc}: {total_length}")
