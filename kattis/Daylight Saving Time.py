# CPU: 0.08 s
from operator import add, sub

for _ in range(int(input())):
    line = input().split()
    char, diff, hour, minute = line[0], *map(int, line[1:])
    op = add if char == "F" else sub
    div, minute = divmod(op(minute, diff), 60)
    hour += div
    hour %= 24
    print(hour, minute)
