# CPU: 0.05 s
amounts = list(map(int, input().split()))
ratios = list(map(int, input().split()))

n = min(amounts[x] / ratios[x] for x in range(3))
for amount, ratio in zip(amounts, ratios):
    print(amount - ratio * n, end=" ")
