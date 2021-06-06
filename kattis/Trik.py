# CPU: 0.05 s
ans = 1
for op in input():
    if op == "A":
        if ans == 1:
            ans = 2
        elif ans == 2:
            ans = 1
    elif op == "B":
        if ans == 2:
            ans = 3
        elif ans == 3:
            ans = 2
    else:
        if ans == 1:
            ans = 3
        elif ans == 3:
            ans = 1
print(ans)
