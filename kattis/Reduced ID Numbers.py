# CPU: 0.42 s
ids = set()
for _ in range(int(input())):
	ids.add(int(input()))

m = 1
while True:
	reduced_ids = set()
	for id_ in ids:
		reduced_id = id_ % m
		if reduced_id not in reduced_ids:
			reduced_ids.add(reduced_id)
		else:
			break
	else:
		break
	m += 1
print(m)
