# CPU: 0.08 s
from sys import stdin

input()
mat = stdin.readlines()
assigned = set()
colors = 0

for idx in range(len(mat[0]) - 1):
	col = set(row[idx] for row in mat)
	for item in col:
		if item in assigned:
			break
	else:
		colors += 1
	assigned = assigned.union(col)
print(colors)