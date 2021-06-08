# CPU: 0.05 s
string = input()
last = ""
ans = ""
for s in string:
    if s != last:
        ans += s
        last = s
print(ans)
