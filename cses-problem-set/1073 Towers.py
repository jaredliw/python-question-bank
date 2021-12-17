# Time: 0.12 s
input()
towers = []  # Store the topmost cube of each tower
for cube in map(int, input().split()):
	# Binary search
	left = 0
	right = len(towers) - 1
	tower_idx = -1
	while left <= right:
		mid = (left + right) // 2
		if towers[mid] <= cube:
			left = mid + 1
		else:
			right = mid - 1
			tower_idx = mid

	if tower_idx != -1:
		towers[tower_idx] = cube
	else:
		towers.append(cube)
print(len(towers))
