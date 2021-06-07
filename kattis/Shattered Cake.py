# CPU: 3.80 s
width = int(input())
area = 0
for _ in range(int(input())):
    w, l = input().split()
    area += int(w) * int(l)
print(area // width)
