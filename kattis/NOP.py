# CPU: 0.05 s
instructions = input()
nop_count = 0
idx = 0
for char in instructions:
    if char.isupper() and idx % 4 != 0:
        add = 4 * (idx // 4 + 1) - idx
        idx += add
        nop_count += add
    idx += 1
print(nop_count)
