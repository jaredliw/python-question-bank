# Time: 0.65 s
from sys import stdin

def flood_fill(x, y):
    global graph

    to_visit = [(x, y)]
    while to_visit:
        x, y = to_visit.pop()
        if 0 <= x < width and 0 <= y < length and graph[x][y] == ".":
            graph[x][y] = "x"
            to_visit.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))

width, length = map(int, stdin.readline().split())
graph = list(map(lambda x: list(x.strip("\n")), stdin.readlines()))

room_count = 0
for row in range(width):
    for col in range(length):
        if graph[row][col] == ".":
            flood_fill(row, col)
            room_count += 1
print(room_count)
