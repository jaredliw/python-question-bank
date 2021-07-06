# CPU: 0.05 s
string = input()
seen = set()
counts = {"P": 13, "K": 13, "H": 13, "T": 13}
for idx in range(0, len(string), 3):
	card = string[idx:idx + 3]
	if card in seen:
		print("GRESKA")
		break
	else:
		seen.add(card)
		counts[card[0]] -= 1
else:
	print(*counts.values())
