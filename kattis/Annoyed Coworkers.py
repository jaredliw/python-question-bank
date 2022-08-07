# CPU: 0.66 s
from heapq import heapify, heapreplace

n_help, n_workers = map(int, input().split())
workers = [list(map(int, input().split())) for _ in range(n_workers)]

predicted = list(map(lambda idx, x: [x[0] + x[1], idx], range(n_workers), workers))
heapify(predicted)

for _ in range(n_help):
    idx = predicted[0][1]
    incr = workers[idx][1]

    workers[idx][0] += incr

    heapreplace(predicted, [predicted[0][0] + incr, idx])

print(max(workers)[0])
