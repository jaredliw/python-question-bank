# CPU: 0.06 s
ranges = []
for _ in range(int(input())):
	ranges.append(tuple(map(int, input().split())))
ranges.sort()

ans = 0
last_end = -1
for start, end in ranges:
	if last_end < start:
		ans += end - start + 1
	else:  # Overlapped
		if end < last_end:  # One range is inside another range
			continue
		ans += end - last_end
	last_end = end
print(ans)
