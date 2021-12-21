# CPU: 0.05 s
def row04():
	output = ".." + "...".join("#" * length) + ".."
	for pos in range(10, len(output), 12):
		output = output[:pos] + "*" + output[pos + 1:]
	print(output)

def row13():
	output = "." + ".".join("#" * length * 2) + "."
	for pos in range(9, len(output), 12):
		output = output[:pos] + "*" + output[pos + 1] + "*" + output[pos + 3:]
	print(output)

def row2():
	output = "...".join("#" * (length + 1))
	if len(word) >= 3:
		for pos in range(8, 8 + 12 * (len(word) // 3), 12):
			output = output[:pos] + "*" + output[pos + 1:pos + 4] + "*" + \
				output[pos + 5:]
	for idx, pos in enumerate(range(2, len(output), 4)):
		output = output[:pos] + word[idx] + output[pos + 1:]
	print(output)

word = input()
length = len(word)
row04()
row13()
row2()
row13()
row04()
