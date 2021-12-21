# CPU: 0.05 s
words = input().split()

n_words_with_ae = 0
for word in words:
    if "ae" in word:
        n_words_with_ae += 1

if n_words_with_ae / len(words) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
