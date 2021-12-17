# Time: 0.30 s
_, goal = map(int, input().split())
machines = list(map(int, input().split()))

lo = 0
hi = 1000000000000000000  # 1e18
ans = 0
while lo <= hi:
	mid = (lo + hi) // 2

	n_produced = 0
	for machine in machines:
		n_produced += mid // machine

	if n_produced >= goal:
		ans = mid
		hi = mid - 1
	else:
		lo = mid + 1
print(ans)
