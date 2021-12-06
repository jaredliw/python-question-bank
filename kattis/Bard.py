# CPU: 0.08 s
n_villagers = int(input())
villagers = {key: set() for key in range(1, n_villagers + 1)}
song_counter = 0
for _ in range(int(input())):
	_, *participants = map(int, input().split())
	if 1 in participants:
		song_counter += 1
		for participant in participants:
			villagers[participant].add(song_counter)
	else:
		for participant in participants:
			for song in villagers[participant]:
				for participant in participants:
					villagers[participant].add(song)

for villager, songs in villagers.items():
	if len(songs) == song_counter:
		print(villager)
