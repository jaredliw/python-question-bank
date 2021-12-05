# CPU: 0.33 s
_, n_lines = map(int, input().split())
locations = list(map(int, input().split()))

for _ in range(n_lines):
	command, arg1, arg2 = map(int, input().split())
	if command == 1:
		locations[arg1 - 1] = arg2
	else:
		print(abs(locations[arg1 - 1] - locations[arg2 - 1]))
