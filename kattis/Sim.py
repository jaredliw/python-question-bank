# CPU: 0.41 s
from collections import deque

for _ in range(int(input())):
    q = deque()  # List is too slow
    pos = 0
    for char in input():
        if char == "<":
            if pos > 0:
                del q[pos - 1]
                pos -= 1
        elif char == "]":
            pos = len(q)
        elif char == "[":
            pos = 0
        else:
            q.insert(pos, char)
            pos += 1
    print("".join(list(q)))
