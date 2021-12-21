# CPU: 0.05 s
nums = [int(input()) for _ in range(9)]
excess = sum(nums) - 100
for num in nums:
    pair = excess - num
    if pair in nums and pair != num:  # All nums are distinct
        nums.remove(num)
        nums.remove(pair)
print(*nums, sep="\n")
