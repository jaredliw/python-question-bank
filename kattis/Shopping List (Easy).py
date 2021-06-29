# CPU: 0.05 s
n, _ = map(int, input().split())
shopping_list = set(input().split())
for _ in range(n - 1):
    shopping_list.intersection_update(set(input().split()))

print(len(shopping_list))
for item in sorted(list(shopping_list)):
    print(item)
