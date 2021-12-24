# CPU: 0.06 s
graph = {}
for _ in range(int(input())):
    node, *adjs = input().split()
    for adj in adjs:
        graph.setdefault(node, set())
        graph[node].add(adj)
        graph.setdefault(adj, set())
        graph[adj].add(node)
fro, to = input().split()

# BFS
visited = set()
paths = [[fro]]  # queue
while paths:
    path = paths.pop()
    node = path[-1]

    if node == to:
        print(*path, sep=" ")
        break
    elif node not in visited:
        if node not in graph:  #!!!
            continue
        for adj in graph[node]:
            if adj not in visited:
                cpy_path = path.copy()
                cpy_path.append(adj)
                paths.append(cpy_path)
        visited.add(node)
else:
    print("no route found")
