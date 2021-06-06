# CPU: 0.05 s
count = 0
for item in input().split(";"):
    if "-" in item:
        start, end = item.split("-")
        count += int(end) - int(start) + 1
    else:
        count += 1
print(count)
