# CPU: 0.06 s
line = input()
length = len(line)

upper_count = 0
lower_count = 0
whitespace_count = 0
symbol_count = 0
for char in line:
    if char == "_":
        whitespace_count += 1
    elif 97 <= ord(char) <= 122:
        lower_count += 1
    elif 65 <= ord(char) <= 90:
        upper_count += 1
    else:
        symbol_count += 1

print(whitespace_count / length)
print(lower_count / length)
print(upper_count / length)
print(symbol_count / length)
