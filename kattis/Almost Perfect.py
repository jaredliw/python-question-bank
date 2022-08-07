# CPU: 0.07 s
import sys
from math import sqrt

for num in sys.stdin.readlines():
  num = int(num)
  divisors_sum = 0
  for d in range(1, int(sqrt(num)) + 1):
    if num % d == 0:
      divisors_sum += d
      another_d = num // d
      if another_d != num and another_d != d:
        divisors_sum += another_d

  if divisors_sum == num:
    print(num, "perfect")
  elif abs(divisors_sum - num) <= 2:
    print(num, "almost perfect")
  else:
    print(num, "not perfect")
