# CPU: 0.05 s
n = int(input())
if n % 2 == 0:
	print((n // 2 + 1) ** 2)
else:
	print((n // 2 + 1) * (n // 2 + 2))
