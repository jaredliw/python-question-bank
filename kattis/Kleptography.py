# CPU: 0.05 s
prefix_length, _ = map(int, input().split())
plaintext = input()[::-1]
ciphertext = input()[::-1]
alphabets = "abcdefghijklmnopqrstuvwxyz"
for idx, char in enumerate(ciphertext[:len(ciphertext) - prefix_length]):
    plaintext += alphabets[(ord(char) - ord(plaintext[idx])) % 26]
print(plaintext[::-1])
