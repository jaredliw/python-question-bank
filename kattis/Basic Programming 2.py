# CPU: 0.18 s
from collections import Counter

length, command = map(int, input().split())
nums = list(map(int, input().split()))

if command == 1:
	nums = set(nums)
	for num in nums:
		if 7777 - num in nums:
			print("Yes")
			break
	else:
		print("No")
elif command == 2:
	if length == len(set(nums)):
		print("Unique")
	else:
		print("Contains duplicate")
elif command == 3:
	most_common = Counter(nums).most_common(1)[0]
	if most_common[1] > length / 2:
		print(most_common[0])
	else:
		print(-1)
elif command == 4:
	nums.sort()
	median_idx = length // 2
	if length % 2 == 0:
		print(*nums[median_idx - 1: median_idx + 1])
	else:
		print(nums[median_idx])
else:
	print(*sorted(filter(lambda x: 100 <= x <= 999, nums)))
