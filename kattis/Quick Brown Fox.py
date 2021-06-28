# CPU: 0.06 s
for _ in range(int(input())):
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    for char in input().lower():
        if char.isalpha() and char in alphabets:
            alphabets.remove(char)
    if alphabets:
        print("missing", "".join(alphabets))
    else:
        print("pangram")
