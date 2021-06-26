# CPU: 0.05 s
name, parent = input().split()

if name[-1] == "e":
    print(name + "x" + parent)
elif name[-1] in "aiou":
    print(name[:-1] + "ex" + parent)
elif name[-2:] == "ex":
    print(name + parent)
else:
    print(name + "ex" + parent)
