# CPU: 0.06 s
n_rows, n_cols = map(int, input().split())
mat = [input() for _ in range(n_rows)]
squash_n = [0, 0, 0, 0, 0]  # Squash 0 ~ 4 cars to park

# Size of monster truck: 2x2
for row in range(n_rows - 1):
	for col in range(n_cols - 1):
		string = mat[row][col:col + 2] + mat[row + 1][col:col + 2]
		if "#" in string:
			continue
		squash_n[string.count("X")] += 1

print(*squash_n, sep="\n")
