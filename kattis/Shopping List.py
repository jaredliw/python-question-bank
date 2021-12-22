# CPU: 0.18 s
n_rows, _ = map(int, input().split())
common_items = set(input().split())
for _ in range(n_rows - 1):
    common_items = common_items.intersection(set(input().split()))
print(len(common_items))
print(*sorted(common_items), sep="\n")
