# CPU: 0.65 s
from itertools import permutations
from math import sqrt

for _ in range(int(input())):
    digits = input()

    primes = set()
    for i in range(1, len(digits) + 1):
        for perm in permutations(digits, i):
            num = int("".join(perm))
            if num <= 1:
                continue

            # Check is prime
            for n in range(2, int(sqrt(num)) + 1):
                if num % n == 0:
                    break
            else:
                primes.add(num)
    print(len(primes))
