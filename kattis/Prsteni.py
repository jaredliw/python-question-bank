# CPU: 0.05 s
def hcf(x, y):
	if x == 0:
		return y
	return hcf(y % x, x)


input()
rings = list(map(int, input().split()))

for idx in range(1, len(rings)):
	factor = hcf(rings[0], rings[idx])
	print(f"{rings[0] // factor}/{rings[idx] // factor}")
