# CPU: 0.06 s
for _ in range(int(input())):
    input()
    places = list(map(int, input().split()))
    print((max(places) - min(places)) * 2)
