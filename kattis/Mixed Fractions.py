# CPU: 0.10 s
while True:
    numerator, denominator = map(int, input().split())
    if numerator == denominator == 0:
        break
    print(*divmod(numerator, denominator), "/", denominator)
