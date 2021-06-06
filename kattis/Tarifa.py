available = int(input())
months = int(input())
available *= months + 1
for _ in range(months):
    available -= int(input())
print(available)
