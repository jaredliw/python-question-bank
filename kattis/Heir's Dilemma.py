# CPU: 0.23 s
count = 0
for num in range(*map(int, input().split())):
    digits = set(str(num))
    if len(digits) != 6:
        continue
    for divisor in map(int, digits):
        if divisor == 0 or num % divisor != 0:
            break
    else:
        count += 1
print(count)
