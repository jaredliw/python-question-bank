# CPU: 0.07 s
while True:
    size = int(input())
    if size == 0:
        break

    string = input().replace(" ", "").upper()
    length = len(string)

    char_arr = [""] * length
    pos = 0
    reset_to = 1
    for char in string:
        char_arr[pos] = char
        pos += size
        if pos >= length:
            pos = reset_to
            reset_to += 1
    print("".join(char_arr))
