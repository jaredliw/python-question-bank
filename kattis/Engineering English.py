# CPU: 0.11 s
from sys import stdin

seen = set()
for line in stdin.readlines():
    for word in line.split():
        if word.lower() not in seen:
            seen.add(word.lower())
            print(word, end=" ")
        else:
            print(". ", end="")
    print()

