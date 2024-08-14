heuristic_cost = {
    'src': 20,
    '1': 22,
    '2': 21,
    '3': 10,
    '4': 25,
    '5': 24,
    '6': 30,
    '7': 5,
    '8': 12,
    'dest': 0
}

graph = {
    'src': ['1', '2', '3'],
    '1': ['4', '5'],
    '2': ['6'],
    '3': ['7', '8'],
    '7': ['dest'],
    '4': [],
    '5': [],
    '6': [],
    '8': [],
    'dest': []
}

def greedy_best_first_search(start, goal):
    open_list = [(heuristic_cost[start], start)]
    came_from = {start: None}
    
    while open_list:
        open_list.sort()
        _, current = open_list.pop(0)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                open_list.append((heuristic_cost[neighbor], neighbor))
    
    return None

def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

start_node = 'src'
goal_node = 'dest'
path = greedy_best_first_search(start_node, goal_node)
print("Path found:", path)

