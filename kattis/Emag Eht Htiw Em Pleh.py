# CPU: 0.06 s
loc = {}
for row in range(2):
    inp = input().split()
    if len(inp) < 2:
        continue
    for piece in inp[1].split(","):
        if len(piece) == 3:
            char = piece[0]
            pos = (ord(piece[1]) - 97, 8 - int(piece[2]))
        else:
            char = "p"
            pos = (ord(piece[0]) - 97, 8 - int(piece[1]))
        char = char.lower() if row == 1 else char.upper()  # Lowercase for black
        loc[pos] = char

print("+---+---+---+---+---+---+---+---+")
for row in range(8):
    print("|", end="")
    for col in range(8):
        decorator = "." if col % 2 == row % 2 else ":"
        pos = (col, row)
        char = loc[pos] if pos in loc else decorator
        print(char.center(3, decorator), end="")
        print("|", end="")
    print("\n+---+---+---+---+---+---+---+---+")
