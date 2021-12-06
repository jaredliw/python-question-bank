# CPU: 0.06 s
for _ in range(int(input())):
	s, d = map(int, input().split())
	# a + b = s => a = s - b
	# a - b = d => a = b + d (assume a >= b)
	# s - b = b + d
	# b = (s - d) / 2
	b = (s - d) / 2
	a = s - b
	if b >= 0 and b.is_integer():
		print(int(a), int(b))
	else:
		print("impossible")
