# CPU: 0.05 s
# d1, d2 = map(int, input().split())
# outcomes = {}
# for n1 in range(1, d1 + 1):
#     for n2 in range(1, d2 + 1):
#         outcomes.setdefault(n1 + n2, 0)
#         outcomes[n1 + n2] += 1
#
# max_ = max(outcomes.values())
# for key, val in outcomes.items():
#     if val == max_:
#         print(key)

# CPU: 0.05 s
d1, d2 = map(int, input().split())
for num in range(min(d1, d2), max(d1, d2) + 1):
    print(num + 1)