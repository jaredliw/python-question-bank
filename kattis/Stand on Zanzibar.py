# CPU: 0.05 s
for _ in range(int(input())):
    population = list(map(int, input().split()))
    import_ = 0
    for idx in range(1, len(population) - 1):
        if population[idx] > population[idx - 1] * 2:
            import_ += population[idx] - population[idx - 1] * 2
    print(import_)
