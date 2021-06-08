# CPU: 0.05 s
secret = set(input())
guesses = input()
incorrect_count = 0
for char in guesses:
    if not secret:
        print("WIN")
        break
    elif incorrect_count == 10:
        print("LOSE")
        break
    elif char in secret:
        secret.remove(char)
    else:
        incorrect_count += 1
