# CPU: 0.13 s
while True:
    lo = 1
    hi = 10
    num = None
    terminate = False
    while True:
        inp = input()
        if inp.isdigit():
            if inp == "0":
                terminate = True
                break
            num = int(inp)
        elif inp == "right on":
            if lo <= num <= hi:
                print("Stan may be honest")
            else:
                print("Stan is dishonest")
            break
        elif inp == "too high":
            hi = min(hi, num - 1)
        else:  # too low
            lo = max(lo, num + 1)

    if terminate:
        break
