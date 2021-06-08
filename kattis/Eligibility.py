# CPU: 0.09 s
for _ in range(int(input())):
    name, study, birth, courses = input().split()
    if int(study[:4]) >= 2010 or int(birth[:4]) >= 1991:
        print(name, "eligible")
    elif int(courses) >= 41:
        print(name, "ineligible")
    else:
        print(name, "coach petitions")
