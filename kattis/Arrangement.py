# CPU: 0.06 s
rooms, teams = int(input()), int(input())
div = teams / rooms
if div.is_integer():
	for _ in range(rooms):
		print("*" * int(div))
else:
	div = int(div) + 1
	more = div * rooms - teams
	for _ in range(rooms - more):
		print("*" * div)
	for _ in range(more):
		print("*" * (div - 1))
