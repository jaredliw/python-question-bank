# CPU: 0.06 s
intervals = []
for _ in range(int(input())):
	intervals.append(list(map(int, input().split())))

# Min. no. of rooms = no. of overlaps + 1
# Sort intervals by L
intervals.sort()

# Reduce multiple nested intervals into one
idx = 1
while idx < len(intervals):
	# If this L >= last U, there is an overlap
	if intervals[idx][0] <= intervals[idx - 1][1]:
		intervals[idx] = [intervals[idx - 1][0], min(intervals[idx - 1][1], intervals[idx][1])]
		intervals.pop(idx - 1)
	else:
		idx += 1
print(len(intervals))
