# CPU: 0.06 s
for testcase in range(int(input())):
    no_ads, ads, cost = list(map(int, input().split()))
    ads -= cost
    if ads > no_ads:
        print('advertise')
    elif ads == no_ads:
        print('does not matter')
    else:
        print('do not advertise')
