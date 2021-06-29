# CPU: 0.06 s
possessed, found, condition = map(int, input().split())
possessed += found
count = 0
while possessed >= condition:
    div, mod = divmod(possessed, condition)
    count += div
    possessed = div + mod
print(count)
