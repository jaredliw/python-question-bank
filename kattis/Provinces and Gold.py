# CPU: 0.05 s
gold, silver, copper = map(int, input().split())

powers = 3 * gold + 2 * silver + 1 * copper
if powers >= 8:
    print("Province or ", end="")
elif powers >= 5:
    print("Duchy or ", end="")
elif powers >= 2:
    print("Estate or ", end="")

if powers >= 6:
    print("Gold")
elif powers >= 3:
    print("Silver")
else:
    print("Copper")
