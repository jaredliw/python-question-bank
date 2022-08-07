# CPU: 0.08 s
first_run = True
while True:
    n_lines = int(input())
    if n_lines == 0:
        break

    if not first_run:
        print()  # Seperate two figures with an empty line

    figure = []
    max_width = 0
    for _ in range(n_lines):
        line = input()
        figure.append(line)
        max_width = max(max_width, len(line))

    rotated = [[] for _ in range(max_width)]
    for row in figure[::-1]:
        for idx, char in enumerate(row.ljust(max_width)):
            if char == "|":
                char = "-"
            elif char == "-":
                char = "|"
            rotated[idx].append(char)

    for row in rotated:
        print("".join(row).rstrip())

    first_run = False
