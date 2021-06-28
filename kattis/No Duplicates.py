# CPU: 0.05 s
words = input().split()
print('yes' if len(words) == len(set(words)) else 'no')
