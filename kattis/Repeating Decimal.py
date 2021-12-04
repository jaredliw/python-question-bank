# CPU: 0.24 s
import sys

for line in sys.stdin.readlines():
	a, b, precision = map(int, line.split())
	ans, a = divmod(a, b)
	ans = str(ans) + "."

	for _ in range(precision):
		a *= 10
		div, a = divmod(a, b)
		ans += str(div)
	print(ans)
