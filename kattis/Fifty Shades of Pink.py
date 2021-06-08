# CPU: 0.07 s
count = 0
for _ in range(int(input())):
    string = input().lower()
    if "pink" in string or "rose" in string:
        count += 1
if count == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(count)
