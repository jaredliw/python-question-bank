# CPU: 0.05 s
from sys import stdin

keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
for line in stdin.readlines():
    for char in line:
        if char not in keyboard:
            print(char, end="")
        else:
            print(keyboard[keyboard.index(char) - 1], end="")
