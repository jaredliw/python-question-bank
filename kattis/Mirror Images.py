# CPU: 0.08 s
from collections import deque

for tc in range(1, int(input()) + 1):
    stack = deque()
    width = int(input().split()[0])
    for _ in range(width):
        stack.append(input()[::-1])

    print("Test", tc)
    for _ in range(width):
        print(stack.pop())
