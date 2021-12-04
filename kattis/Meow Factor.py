# CPU: 0.05 s
n = int(input())
for num in range(int(n ** (1 / 9)) + 1, 0, -1):
	if n % num ** 9 == 0:
		print(num)
		break
