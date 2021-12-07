# CPU: 0.09 s
counter = [0, 0, 0, 0]
cur_type = None
byte_length = None
for _ in range(int(input())):
	byte = input()
	if cur_type is None:
		if byte.startswith("0"):
			counter[0] += 1
		else:
			for type_, valid_prefix in enumerate(["110", "1110", "11110"], 1):
				if byte.startswith(valid_prefix):
					cur_type = type_
					byte_length = type_
					break
			else:
				print("invalid")
				break
	else:
		if byte.startswith("10"):
			byte_length -= 1
			if byte_length == 0:
				counter[cur_type] += 1
				cur_type = None
				byte_length = None
			elif cur_type < 0:
				print("invalid")
				break
		else:
			print("invalid")
			break
else:
	invalid = False
	if cur_type is not None:
		if byte_length > 0:
			print("invalid")
			invalid = True
		else:
			counter[cur_type] += 1

	if not invalid:
		print(*counter, sep="\n")
