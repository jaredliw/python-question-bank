# CPU: 0.09 s
least_incorrect_idx = None
least_incorrect = float("inf")
for idx in range(1, int(input().split()[0]) + 1):
	seq = input().split()
	incorrect_count = 0
	for num, actual in enumerate(seq, 1):
		expected = ""
		divisible = False
		if num % 3 == 0:
			expected += "fizz"
			divisible = True
		if num % 5 == 0:
			expected += "buzz"
			divisible = True
		if not divisible:
			expected = str(num)

		if expected != actual:
			incorrect_count += 1
	
	if incorrect_count < least_incorrect:
		least_incorrect = incorrect_count
		least_incorrect_idx = idx
print(least_incorrect_idx)
