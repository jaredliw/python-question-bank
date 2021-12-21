# CPU: 0.05 s
a, b, c = map(int, input().split())
# Max gap between any two kangaroos
print(max(b - a - 1, c - b - 1))
