# CPU: 0.05 s
hashmap = {}
for card in input().split():
    hashmap.setdefault(card[0], 0)
    hashmap[card[0]] += 1
print(max(hashmap.values()))
