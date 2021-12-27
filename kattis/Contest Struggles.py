# CPU: 0.06 s
n_total, n_solved = map(int, input().split())
avg, avg_solved = map(int, input().split())
ans = (n_total * avg - n_solved * avg_solved) / (n_total - n_solved)
print(ans if 0 <= ans <= 100 else "impossible")
