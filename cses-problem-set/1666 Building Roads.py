# Time: 0.67 s
n_nodes, n_lines = map(int, input().split())
adj = [set() for _ in range(n_nodes)]
for _ in range(n_lines):
	node1, node2 = map(lambda x: int(x) - 1, input().split())
	adj[node1].add(node2)
	adj[node2].add(node1)

visited = set()
start_nodes = set()  # One node per connected component
for start_node in range(n_nodes):
	if start_node not in visited:
		# Start DFS
		to_visit = set([start_node])
		while to_visit:
			cur_node = to_visit.pop()
			visited.add(cur_node)
			for adj_node in adj[cur_node]:
				if adj_node not in visited:
					to_visit.add(adj_node)
		# End DFS
		start_nodes.add(start_node)

print(len(start_nodes) - 1)  # No. of connected components - 1
ref_node = start_nodes.pop()
for node in start_nodes:
	print(ref_node + 1, node + 1)  # 1-indexed
