# CPU: 0.13 s
from collections import Counter

# Double for loop does not work: TLE
n_nums, divisor = map(int, input().split())
nums = Counter(map(lambda x: int(x) // divisor, input().split()))
print(sum(map(lambda x: x * (x - 1) // 2, nums.values())))

# CPU: 0.13 s
# n_nums, divisor = map(int, input().split())
# nums = list(map(int, input().split()))
# nums.sort()
#
# count = 0
# last_quotient = nums[0] // divisor
# cur_quotient_count = 1
# for num in nums[1:]:
# 	quotient = num // divisor
# 	if quotient > last_quotient:
# 		count += cur_quotient_count * (cur_quotient_count - 1) // 2
# 		last_quotient = quotient
# 		cur_quotient_count = 1
# 	else:
# 		cur_quotient_count += 1
# count += cur_quotient_count * (cur_quotient_count - 1) // 2
# print(count)
