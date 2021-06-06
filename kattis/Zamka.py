# CPU: 0.06 s
def sum_digits(x):
    cur_sum_d = 0
    while x != 0:
        cur_sum_d += x % 10
        x //= 10
    return cur_sum_d


min_, max_, sum_d = int(input()), int(input()), int(input())
for num in range(min_, max_ + 1):
    if sum_digits(num) == sum_d:
        print(num)
        break

for num in range(max_, min_ - 1, -1):
    if sum_digits(num) == sum_d:
        print(num)
        break
