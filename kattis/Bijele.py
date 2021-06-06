# CPU: 0.05 s
correct = (1, 1, 2, 2, 2, 8)
for idx, piece in enumerate(input().split()):
    print(correct[idx] - int(piece), end=' ')
