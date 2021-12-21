# CPU: 0.05 s
a = input()
b = input()
ans = a.count("S") * b.count("S")
print("S(" * ans + "0" + ")" * ans)
