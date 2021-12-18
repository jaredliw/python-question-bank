# CPU: 0.07 s
def to_int(string):
	sum_ = 0
	for char in string:
		sum_ += ord(char) - 65
	return sum_

def rotate(string, key):
	rotated = ""
	for idx, char in enumerate(string):
		if isinstance(key, str):
			n = to_int(key[idx])
		else:
			n = key
		rotated += chr(65 + (ord(char) - 65 + n) % 26)
	return rotated

cipher = input()
# Divide
half = len(cipher) // 2  # The cipher is always even
chunk1, chunk2 = cipher[:half], cipher[half:]
# Rotate
rotated1, rotated2 = rotate(chunk1, to_int(chunk1)), rotate(chunk2, to_int(chunk2))
# Merge
print(rotate(rotated1, rotated2))
