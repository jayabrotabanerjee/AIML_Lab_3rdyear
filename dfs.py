def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start_node)
    dfs_order = [start_node]
    
    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            dfs_order.extend(dfs(graph, neighbor, visited))
    
    return dfs_order

graph = {
    1: [2, 7, 8],
    2: [3, 6],
    7: [],
    8: [9, 12],
    3: [4, 5],
    6: [],
    9: [10, 11],
    12: [],
    4: [],
    5: [],
    10: [],
    11: []
}

dfs_order = dfs(graph, 1)
print("DFS traversal order:", dfs_order)

