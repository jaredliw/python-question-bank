# CPU: 0.06 s
from functools import reduce
from itertools import count

for num in count(int(input())):
    sum_digits = reduce(lambda accum, x: accum + int(x), str(num), 0)
    if num % sum_digits == 0:
        print(num)
        break
