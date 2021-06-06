# Naive solution:
# iterations = int(input())
# step = 1
# points = 2
# for iteration in range(iterations):
#     points += step
#     step *= 2
# print(points ** 2)

# CPU: 0.05 s
print((2 ** int(input()) + 1) ** 2)
