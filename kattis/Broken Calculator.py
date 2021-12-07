# CPU: 0.08 s
from math import ceil

prev_ans = 1
for _ in range(int(input())):
	operand1, operator, operand2 = input().split()
	operand1 = int(operand1)
	operand2 = int(operand2)

	if operator == "+":
		ans = operand1 + operand2 - prev_ans
	elif operator == "-":
		ans = (operand1 - operand2) * prev_ans
	elif operator == "*":
		ans = (operand1 * operand2)  ** 2
	else:
		ans = ceil(operand1 / 2)
	print(ans)
	prev_ans = ans
