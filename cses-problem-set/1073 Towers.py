# Time: 0.14 s
from bisect import bisect

input()
# Store the topmost cube of each tower
# Towers are in non-decreasing order for sure
towers = []
for cube in map(int, input().split()):
	tower_idx = bisect(towers, cube)

	# If there exists a satisfying tower, add the cube to that tower
	# and update the top element of the tower
	if tower_idx < len(towers):
		towers[tower_idx] = cube
	# If there aren't any suitable towers, append new tower to end of
	# array
	else:
		towers.append(cube)
print(len(towers))


# Time: 0.12 s
# input()
# # Store the topmost cube of each tower
# # Towers are in non-decreasing order for sure
# towers = []
# for cube in map(int, input().split()):
# 	# Binary search
# 	left = 0
# 	right = len(towers) - 1
# 	tower_idx = -1
# 	while left <= right:
# 		mid = (left + right) // 2
# 		if towers[mid] <= cube:
# 			left = mid + 1
# 		else:
# 			right = mid - 1
# 			tower_idx = mid

# 	# If there exists a satisfying tower, add the cube to that tower
# 	# and update the top element of the tower
# 	if tower_idx != -1:
# 		towers[tower_idx] = cube
# 	# If there aren't any suitable towers, append new tower to end of
# 	# array
# 	else:
# 		towers.append(cube)
# print(len(towers))
