# CPU: 0.06 s
string = input()
for pattern in [":)", ";)", ":-)", ";-)"]:
	start_idx = 0
	while True:
		result = string.find(pattern, start_idx)
		if result == -1:
			break
		print(result)
		start_idx = result + 1
