# CPU: 0.10 s
n = int(input())

horiz = []
vert = []
diag1 = []
diag2 = []
for _ in range(n):
    x, y = map(int, input().split())
    d1 = x + y
    d2 = n - x + y
    if x in horiz or y in vert or d1 in diag1 or d2 in diag2:
        print("INCORRECT")
        break
    horiz.append(x)
    vert.append(y)
    diag1.append(d1)
    diag2.append(d2)
else:
    print("CORRECT")
