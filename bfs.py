def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    bfs_order = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return bfs_order

graph = {
    'B': ['E', 'X', 'K'],
    'E': ['P', 'G'],
    'X': [],
    'K': ['A', 'R'],
    'P': ['D', 'T'],
    'G': [],
    'A': ['H', 'M'],
    'R': [],
    'D': [],
    'T': [],
    'H': [],
    'M': []
}

bfs_order = bfs(graph, 'B')
print("BFS traversal order:", bfs_order)

