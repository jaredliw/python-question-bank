# CPU: 0.10 s
records = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for _ in range(int(input())):
	is_vaccinated, *status = map(lambda x: x == "Y", input())
	for idx, is_infected in enumerate(status):
		if is_vaccinated:
			if is_infected:
				records[idx][0] += 1
			records[idx][1] += 1
		else:
			if is_infected:
				records[idx][2] += 1
			records[idx][3] += 1

for vaccinated_infected, vaccinated_total, not_vaccinated_infected, not_vaccinated_total in records:
	vaccinated_infection_rate = vaccinated_infected / vaccinated_total * 100
	not_vaccinated_infection_rate = not_vaccinated_infected / not_vaccinated_total * 100
	efficacy = 100 - vaccinated_infection_rate * 100 / not_vaccinated_infection_rate

	if efficacy > 0:
		print(efficacy)
	else:
		print("Not Effective")
