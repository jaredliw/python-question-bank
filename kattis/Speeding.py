# CPU: 0.06 s
photos = []
for _ in range(int(input())):
	photos.append(list(map(int, input().split())))

speeds = []
for idx in range(1, len(photos)):
	speeds.append((photos[idx][1] - photos[idx - 1][1]) / (photos[idx][0] - photos[idx - 1][0]))

print(int(max(speeds)))
