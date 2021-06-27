# CPU: 0.05 s
n = int(input())

if n % 2 == 0:
	if (n // 2) % 2 == 0:
		print("even")
	else:
		print("odd")
else:
	print("either")
