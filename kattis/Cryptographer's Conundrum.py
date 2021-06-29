# CPU: 0.06 s
text = input()
target = "PER"
count = 0
for idx, char in enumerate(text):
    if char != target[idx % 3]:
        count += 1
print(count)
