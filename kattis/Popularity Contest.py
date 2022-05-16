# CPU: 0.59 s
n_people, n_pairs = map(int, input().split())
popularity_factors = {}
for i in range(1, n_people + 1):
    popularity_factors[i] = 0

for _ in range(n_pairs):
    a, b = map(int, input().split())
    popularity_factors[a] += 1
    popularity_factors[b] += 1

for success_factor, popularity_factor in popularity_factors.items():
    print(popularity_factor - success_factor, end=" ")
