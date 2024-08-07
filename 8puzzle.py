def print_state(state):
    """ Print the 3x3 grid state """
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def get_neighbors(state):
    """ Return a list of possible states from the current state """
    neighbors = []
    blank_index = state.index(None)
    row, col = divmod(blank_index, 3)
    
    moves = {
        -1: "left", 
        1: "right", 
        -3: "up", 
        3: "down"
    }
    
    for move in moves.keys():
        new_index = blank_index + move
        if move == -1 and col == 0: continue
        if move == 1 and col == 2: continue
        if move == -3 and row == 0: continue
        if move == 3 and row == 2: continue
        
        if 0 <= new_index < 9:
            new_state = list(state)
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            neighbors.append(tuple(new_state))
    
    return neighbors

def bfs(start, goal):
    """ Perform BFS to find the shortest path from start to goal """
    queue = [(start, [])]
    visited = set()
    visited.add(start)
    
    while queue:
        current_state, path = queue.pop(0)
        
        if current_state == goal:
            return path + [current_state]
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current_state]))
    
    return None

def main():
    initial_state = (2, 8, 3, 1, 6, 4, 7, None, 5)
    final_state = (1, 2, 3, 8, None, 4, 7, 6, 5)
    
    print("Initial State:")
    print_state(initial_state)
    
    print("Final State:")
    print_state(final_state)
    
    solution_path = bfs(initial_state, final_state)
    
    if solution_path:
        print(f"Solution found in {len(solution_path) - 1} moves:")
        for step in solution_path:
            print_state(step)
    else:
        print("No solution found")

if __name__ == "__main__":
    main()

