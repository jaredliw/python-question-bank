# CPU: 0.14 s
leg_a, leg_b, leg_c, total = map(int, input().split())
possible = False
for a in range(total // leg_a + 1):
	for b in range(total // leg_b + 1):
		for c in range(total // leg_c + 1):
			if leg_a * a + leg_b * b + leg_c * c == total:
				print(a, b, c)
				possible = True
if not possible:
	print("impossible")
