# CPU: 0.05 s
from sys import stdin

mapping = {
	0: 'zero',
	1: 'one', 
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen', 
    16: 'sixteen', 
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

for line in stdin.readlines():
	words = line.split()
	for idx, word in enumerate(words):
		if word.isdigit():
			word = int(word)
			if word in mapping:
				word = mapping[word]
			else:
				tenths, ones = divmod(word, 10)
				tenths *= 10
				word = mapping[tenths] + "-" + mapping[ones]

			if idx == 0:
				word = word.capitalize()
			words[idx] = word
	print(*words)
