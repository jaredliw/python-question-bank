# CPU: 0.05 s
mapping = {
    "***\n* *\n* *\n* *\n***\n": "0",
    "  *\n  *\n  *\n  *\n  *\n": "1",
    "***\n  *\n***\n*  \n***\n": "2",
    "***\n  *\n***\n  *\n***\n": "3",
    "* *\n* *\n***\n  *\n  *\n": "4",
    "***\n*  \n***\n  *\n***\n": "5",
    "***\n*  \n***\n* *\n***\n": "6",
    "***\n  *\n  *\n  *\n  *\n": "7",
    "***\n* *\n***\n* *\n***\n": "8",
    "***\n* *\n***\n  *\n***\n": "9",
}

digits = []
for _ in range(5):
    segments = []
    # Split string
    string = ""
    for idx, char in enumerate(input()):
        if idx != 0 and (idx + 1) % 4 == 0:
            segments.append(string)
            string = ""
        else:
            string += char
    segments.append(string)

    for idx, segment in enumerate(segments):
        if idx >= len(digits):
            digits.append("")
        digits[idx] += segment + "\n"

num = ""
for digit in digits:
    try:
        num += mapping[digit]
    except KeyError:
        num = -1
        break

if int(num) % 6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")
