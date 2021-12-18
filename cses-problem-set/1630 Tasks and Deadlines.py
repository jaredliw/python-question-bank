# Time: 0.88 s
from sys import stdin

# Do not read input line by line, TLE
lines = stdin.readlines()
tasks = []
for line in lines[1:]:
	tasks.append(tuple(map(int, line.split())))
# The optimal solution to the problem does not depend on the deadlines at all,
# read https://usaco.guide/CPH.pdf#page=70 for more details
tasks.sort()

cur_time = 0
reward = 0
for task, deadline in tasks:
	cur_time += task
	reward += deadline - cur_time
print(reward)
