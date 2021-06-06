n_judges, n_ratings = map(int, input().split())
sum_ = 0
for _ in range(n_ratings):
    sum_ += int(input())
print((sum_ + (n_judges - n_ratings) * -3) / n_judges, (sum_ + (n_judges - n_ratings) * 3) / n_judges)
