# CPU: 0.06 s
input()
lineup = list(map(int, input().split()))
if lineup == []:
	ans = []
else:
	ans , _ = zip(*sorted(enumerate(lineup, 2), key=lambda x: x[1]))
print(1, *ans)  # Jimmy is always the first
