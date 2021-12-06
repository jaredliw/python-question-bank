# CPU: 0.44 s
n_teams, win_score, n_records = map(int, input().split())

scoreboard = {}
for _ in range(n_teams):
    scoreboard[input()] = 0

has_winner = False
for _ in range(n_records):
    team, score = input().split()
    if team in scoreboard:
        scoreboard[team] += int(score)

        if scoreboard[team] >= win_score:
            print(team, "wins!")
            has_winner = True
            del scoreboard[team]

if not has_winner:
    print("No winner!")

