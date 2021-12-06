# CPU: 0.11 s
memory = {}
while True:
	statement = input()
	if statement == "0":
		break

	if "=" in statement:
		var, val = statement.split(" = ")
		memory[var] = val
	else:
		operands = statement.split(" + ")
		numerical_sum = 0
		simplified = []
		for idx, operand in enumerate(operands):
			if operand in memory:
				operand = memory[operand]
			if operand.isdigit():
				numerical_sum += int(operand)
			else:
				simplified.append(operand)

		if numerical_sum != 0:
			simplified.insert(0, numerical_sum)
		print(*simplified, sep=" + ")
