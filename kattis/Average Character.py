# CPU: 0.04 s
string = input()
print(chr(sum(ord(char) for char in string) // len(string)))
