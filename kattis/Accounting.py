# CPU: 0.58 s
_, n_lines = map(int, input().split())

general_wealth = 0
special_cases = {}
for _ in range(n_lines):
  command, *args = input().split()
  if command == "RESTART":
    general_wealth = int(args[0])
    special_cases.clear()
  elif command == "PRINT":
    n = int(args[0])
    print(special_cases[n] if n in special_cases else general_wealth)
  else:
    special_cases[int(args[0])] = int(args[1])
