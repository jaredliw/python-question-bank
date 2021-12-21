# CPU: 0.06 s
cipher = input()
key = input()

plain = ""
for idx in range(len(cipher)):
    cord = ord(cipher[idx]) - 65
    kord = ord(key[idx]) - 65
    pchar = chr(65 + (cord - kord) % 26)
    plain += pchar
    key += pchar
print(plain)
