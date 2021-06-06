# CPU: 0.05 s
max_x, max_y, x, y = map(int, input().split())
print(int(max_x - 2 >= x and max_y - 2 >= y))
