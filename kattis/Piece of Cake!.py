# CPU: 0.06 s
n, h, v = map(int, input().split())
print(max(h, n - h) * max(v, n - v) * 4)
