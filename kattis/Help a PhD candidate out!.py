# CPU: 0.09 s
for _ in range(int(input())):
    inp = input()
    if inp == "P=NP":
        print("skipped")
    else:
        print(eval(inp))
