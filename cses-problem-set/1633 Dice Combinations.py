# Time: 0.19 s
dp = [1]
for i in range(int(input())):
	dp.append(sum(dp[-6:]) % 1000000007)
print(dp[-1])
