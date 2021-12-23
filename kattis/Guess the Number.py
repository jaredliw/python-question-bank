# CPU: 0.06 s
lo = 1
hi = 1000
while lo <= hi:
    mid = (lo + hi) // 2
    print(mid)

    response = input()
    if response == "correct":
        break
    elif response == "lower":
        hi = mid - 1
    else:
        lo = mid + 1
