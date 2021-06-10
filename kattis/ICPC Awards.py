# CPU: 0.05 s
universities = set()
for _ in range(int(input())):
    university, name = input().split()
    if len(universities) >= 12:
        break
    elif university not in universities:
        print(university, name)
        universities.add(university)
