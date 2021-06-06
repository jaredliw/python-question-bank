# CPU: 0.06 s
x, y, n = map(int, input().split())
for num in range(1, n+1):
    divisible = False
    if num % x == 0:
        print('Fizz', end='')
        divisible = True
    if num % y == 0:
        print('Buzz', end='')
        divisible = True
    if not divisible:
        print(num, end='')
    print()
