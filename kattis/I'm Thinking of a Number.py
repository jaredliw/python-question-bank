# CPU: 0.20 s
while True:
	no_of_lines = int(input())
	if no_of_lines == 0:
		break

	lower_bound = 1
	upper_bound = float("inf")
	divisibility = []
	for _ in range(no_of_lines):
		*words, num = input().split()
		num = int(num)

		# min and max functions are key points to pass all test cases!
		if words[0] == "less":
			upper_bound = min(upper_bound, num)
		elif words[0] == "greater":
			lower_bound = max(lower_bound, num + 1)
		else:
			divisibility.append(num)

	if upper_bound == float("inf"):
		print("infinite")
	else:
		ans = []
		for num in range(lower_bound, upper_bound):
			for divisor in divisibility:
				if num % divisor != 0:
					break
			else:		
				ans.append(num)

		if ans:
			print(*ans)
		else:
			print("none")
