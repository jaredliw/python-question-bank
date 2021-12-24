# CPU: 0.06 s
from math import ceil

n, target = map(int, input().split())
if target == 100:
    print("impossible")
else:
    sum_score = sum(map(int, input().split()))
    # Solve:
    # (sum_score + 100 * n) / (n + ans) >= target
    print(ceil((target * n - sum_score) / (100 - target)))
