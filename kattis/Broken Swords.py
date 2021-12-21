# CPU: 0.12 s
tb_count = 0
lr_count = 0
for _ in range(int(input())):
    inp = input()
    tb_count += inp[:2].count("0")
    lr_count += inp[2:].count("0")

n_swords = min(tb_count, lr_count) // 2
print(n_swords, tb_count - 2 * n_swords, lr_count - 2 * n_swords)
