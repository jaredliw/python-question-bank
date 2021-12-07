# CPU: 0.05 s
seq_sum = 0
def h(n):
	global seq_sum
	seq_sum += n
	if n == 1:
		return 1
	elif n % 2 == 0:
		return h(n // 2)
	else:
		return h(3 * n + 1)

h(int(input()))
print(seq_sum)
