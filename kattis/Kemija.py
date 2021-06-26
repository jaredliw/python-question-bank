# CPU: 0.05 s
sentence = input()
idx = 0
while idx < len(sentence):
    print(sentence[idx], end="")
    if sentence[idx] in "aeiou":
        idx += 2
    idx += 1
