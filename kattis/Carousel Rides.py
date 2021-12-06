# CPU: 0.07 s
while True:
	n_lines, max_buy = map(int, input().split())
	if n_lines == max_buy == 0:
		break

	best_offer = None
	best_price_per_ticket = float("inf")
	for _ in range(n_lines):
		n_tickets, price = map(int, input().split())
		if n_tickets <= max_buy:
			price_per_ticket = price / n_tickets
			if price_per_ticket < best_price_per_ticket or (price_per_ticket == best_price_per_ticket and n_tickets > best_offer[0]):
				best_offer = (n_tickets, price)
				best_price_per_ticket = price_per_ticket

	if best_offer is None:
		print("No suitable tickets offered")
	else:
		print("Buy {} tickets for ${}".format(*best_offer))
