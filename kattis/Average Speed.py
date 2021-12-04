# CPU: 0.05 s
import sys

time = 0  # in hours
speed = 0
distance = 0
for line in sys.stdin.readlines():
	chunks = line.split()
	h, m, s = map(int, chunks[0].split(":"))
	cur_time = h + m / 60 + s / 3600
	time_diff = cur_time - time
	distance += time_diff * speed
	# Check this line is a statement or a query
	if len(chunks) > 1:
		speed = int(chunks[1])
	else:
		print(f"{chunks[0]} {distance:.2f} km")
	time = cur_time
