# CPU: 0.09 s
dates = {}
for _ in range(int(input())):
	name, degree, date = input().split()
	degree = int(degree)

	if date not in dates or dates[date][0] < degree:
		dates[date] = (degree, name)
_, names = zip(*dates.values())
print(len(names))
print(*sorted(names), sep="\n")
