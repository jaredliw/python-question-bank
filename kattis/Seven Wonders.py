# CPU: 0.05 s
tablet = 0
compass = 0
gear = 0
for char in input():
    if char == "T":
        tablet += 1
    elif char == "C":
        compass += 1
    else:
        gear += 1
print(tablet ** 2 + compass ** 2 + gear ** 2 + min(tablet, compass, gear) * 7)
