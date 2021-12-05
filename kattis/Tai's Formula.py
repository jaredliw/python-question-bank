# CPU: 0.11 s
records = [list(map(float, input().split())) for _ in range(int(input()))]

area = 0
for idx in range(1, len(records)):
	area += 0.5 * (records[idx][1] + records[idx - 1][1]) * (records[idx][0] - records[idx - 1][0])
print(area / 1000)