# CPU: 0.05 s
# print(int(str(bin(int(input())).lstrip('0b'))[::-1], 2))

# CPU: 0.05 s
n = int(input())
ans = 0
while n != 0:
    ans <<= 1
    ans += n & 1
    n >>= 1
print(ans)