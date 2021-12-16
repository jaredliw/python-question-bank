# Time: 0.14 s
_, k = map(int, input().split())
nums = map(int, input().split())
 
prefix_count = {0: 1}
sum_ = 0
ans = 0
for num in nums:
    sum_ += num
 
    try:
        ans += prefix_count[sum_ - k]
    except KeyError:
        pass
    
    prefix_count.setdefault(sum_, 0)
    prefix_count[sum_] += 1
print(ans)
