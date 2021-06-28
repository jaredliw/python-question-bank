missed = False
last = 0
for _ in range(int(input())):
    cur = int(input())
    for num in range(last + 1, cur):
        print(num)
        missed = True
    last = cur

if not missed:
    print("good job")
