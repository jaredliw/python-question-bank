# CPU: 0.05 s
string = input()
substr_len = len(string) // 3
if string[:substr_len] == string[substr_len:substr_len * 2] or string[:substr_len] == string[substr_len * 2:]:
    print(string[:substr_len])
else:
    print(string[substr_len:substr_len * 2])
