# CPU: 0.62 s
n_nodes, n_edges = map(int, input().split())
graph = [set() for _ in range(n_nodes)]
for _ in range(n_edges):
    fro, to = map(int, input().split())
    graph[fro - 1].add(to - 1)  # 0-indexed
    graph[to - 1].add(fro - 1)

# DFS
to_visit = {0}
visited = set()
while to_visit:
    node = to_visit.pop() + 1  # 1-indexed
    if node not in visited:
        visited.add(node)
        for adj in graph[node - 1]:  # 0-indexed
            to_visit.add(adj)

if len(visited) == n_nodes:
    print("Connected")
else:
    print(*sorted(set(range(1, n_nodes + 1)) - visited), sep="\n")
