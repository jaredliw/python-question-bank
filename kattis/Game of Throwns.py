# CPU: 0.06 s
from collections import deque

n_students, _ = map(int, input().split())
commands = input().split()

undo_op = False
history = deque([0])  # Using as a stack here
for command in commands:
	if command.isalpha():
		undo_op = True
	elif undo_op:
		for _ in range(int(command)):
			history.pop()
		undo_op = False
	else:
		history.append((history[-1] + int(command)) % n_students)
print(history[-1])
