# CPU: 0.02 s
nums = int(input())
ans = 0
for x in range(nums):
    num = input()
    ans += int(num[:-1]) ** int(num[-1])
print(ans)
