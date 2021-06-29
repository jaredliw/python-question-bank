# CPU: 0.05 s
from operator import add, sub

ciphertext = input()
key = input()
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = ""
for idx in range(len(ciphertext)):
    if idx % 2 == 0:
        op = sub
    else:
        op = add
    plaintext += alphabets[op(alphabets.index(ciphertext[idx]), alphabets.index(key[idx])) % 26]
print(plaintext)
