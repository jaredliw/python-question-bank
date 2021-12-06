# CPU: 0.06 s
for _ in range(int(input())):
	tc_no, num = input().split()
	try:
		oct_num = int(num, 8)
	except ValueError:
		oct_num = 0
	# Idk why but you have to convert num to int before printing (or else 'Wrong answer')
	print(tc_no, oct_num, int(num), int(num, 16))
