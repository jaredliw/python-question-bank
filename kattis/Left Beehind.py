# CPU: 0.05 s
while True:
    sweet, sour = map(int, input().split())
    if sweet == sour == 0:
        break

    if sweet + sour == 13:
        print("Never speak again.")
    elif sweet > sour:
        print("To the convention.")
    elif sweet == sour:
        print("Undecided.")
    else:
        print("Left beehind.")
