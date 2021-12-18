# CPU: 0.06 s
from collections import deque

input()
values = list(map(lambda x: x == "T", input().split()))
queue = deque(map(lambda x: values[ord(x) - 65] if x.isalpha() else x,
	input().split()))

register = deque()
while len(queue) > 0:
	op = queue.popleft()

	if isinstance(op, int):
		register.append(op)
	# Use bitwise operators (&, |), not logic operators (and, or)
	else:
		if op == "*":
			register.append(register.pop() & register.pop())
		elif op == "+":
			register.append(register.pop() | register.pop())
		else:
			register.append(not register.pop())

		if len(queue) == 1 and isinstance(queue[0], bool):
			break

print("T" if register.pop() else "F")
