# CPU: 0.06 s
from functools import reduce

for test_case in range(int(input())):
    input()
    print("Case #{}: {}".format(test_case + 1, reduce(lambda x, y: x ^ y, map(int, input().split()))))

# CPU: 0.06 s
# for test_case in range(int(input())):
#     input()
#     guests = list(map(int, input().split()))
#     print("Case #{}: {}".format(test_case + 1, sum(set(guests)) * 2 - sum(guests)))
