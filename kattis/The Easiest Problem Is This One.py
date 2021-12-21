# CPU: 0.09 s
from itertools import count
from functools import reduce

calc = lambda accum, x: accum + int(x)
while True:
    num = int(input())
    if num == 0:
        break

    digit_sum = reduce(calc, str(num), 0)
    for mul in count(11):
        if digit_sum == reduce(calc, str(num * mul), 0):
            print(mul)
            break
