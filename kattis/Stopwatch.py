# CPU: 0.07 s
n = int(input())
if n % 2 == 1:
    print("still running")
else:
    sum_ = 0
    for _ in range(n // 2):
        sum_ -= int(input()) - int(input())
    print(sum_)
