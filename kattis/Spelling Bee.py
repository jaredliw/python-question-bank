# CPU: 0.24 s
inp = input()
center_letter = inp[0]
letters = set(inp)
for _ in range(int(input())):
    word = input()
    if len(word) >= 4 and center_letter in word and set(word).issubset(letters):
        print(word)
