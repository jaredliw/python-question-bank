# CPU: 0.06 s
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
    90: 'ninety',
}

def num_to_word(n):
    if n in mapping:
        return mapping[n]

    hundreds, tens_ones = divmod(n, 100)
    if hundreds == 0:
        tenths, ones = divmod(tens_ones, 10)
        return mapping[tenths * 10] + mapping[ones]
    else:
        text = num_to_word(hundreds) + "hundred"
        if tens_ones != 0:
            text += num_to_word(tens_ones)
        return text

char_count = 0
words = []
for _ in range(int(input())):
    word = input()
    if word != "$":
        char_count += len(word)
    words.append(word)
words = " ".join(words)

for num in range(3, 1000):
    word_num = num_to_word(num)

    if len(word_num) + char_count == num:
        print(words.replace("$", word_num))
        break
