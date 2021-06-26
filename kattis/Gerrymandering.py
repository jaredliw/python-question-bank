# CPU: 0.12 s
line, count = map(int, input().split())
a_wasted = 0
b_wasted = 0
total = 0
districts = [[0, 0] for _ in range(count)]
for _ in range(line):
    idx, a, b = map(int, input().split())
    districts[idx - 1][0] += a
    districts[idx - 1][1] += b

for district in districts:
    total += district[0] + district[1]
    if district[0] > district[1]:
        a, b = district[0] - (district[0] + district[1]) // 2 - 1, district[1]
        a_wasted += a
        b_wasted += b
        print("A", a, b)
    else:
        a, b = district[0], district[1] - (district[0] + district[1]) // 2 - 1
        a_wasted += a
        b_wasted += b
        print("B", a, b)
print(abs(a_wasted - b_wasted) / total)
