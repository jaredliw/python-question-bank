# CPU: 0.14 s
for _ in range(int(input())):
    str1 = input()
    str2 = input()
    print(str1)
    print(str2)
    for char1, char2 in zip(str1, str2):
        print("." if char1 == char2 else "*", end="")
    print("\n")
