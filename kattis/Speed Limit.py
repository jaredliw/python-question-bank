# CPU: 0.05 s
while True:
    n = int(input())
    if n == -1:
        break
    last = 0
    total = 0
    for _ in range(int(n)):
        speed, time = map(int, input().split())
        total += speed * (time - last)
        last = time
    print(total, "miles")
