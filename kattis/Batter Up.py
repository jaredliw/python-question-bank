# CPU: 0.05 s
input()
marks = list(filter(lambda x: x != -1, map(int, input().split())))
print(sum(marks) / len(marks))
