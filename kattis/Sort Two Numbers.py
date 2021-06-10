# CPU: 0.05 s
a, b = map(int, input().split())
if a > b:
    a, b = b, a
print(a, b)
