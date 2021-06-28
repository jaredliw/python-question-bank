# CPU: 0.06 s
for _ in range(int(input())):
    gnomes = list(map(int, input().split()))[1:]
    for idx in range(1, len(gnomes)):
        if gnomes[idx] != gnomes[idx - 1] + 1:
            print(idx + 1)
            break
