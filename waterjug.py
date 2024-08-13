import uuid
from collections import deque

def get_mac_address():
    """Retrieve the MAC address of the machine."""
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                    for elements in range(0, 2*6, 2)][::-1])
    return mac

def water_jug_problem(capacity1, capacity2, target):
    """Solve the water jug problem using BFS."""
    initial_state = (0, 0)  # Both jugs are empty initially
    visited = set()
    queue = deque([(initial_state, [])])
    
    while queue:
        (jug1, jug2), path = queue.popleft()
        
        # Check if we have reached the target
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]
        
        # Mark the state as visited
        visited.add((jug1, jug2))
        
        # Possible state transitions
        possible_states = [
            (capacity1, jug2),  # Fill jug1
            (jug1, capacity2),  # Fill jug2
            (0, jug2),          # Empty jug1
            (jug1, 0),          # Empty jug2
            (min(capacity1, jug1 + jug2), jug2 - (min(capacity1, jug1 + jug2) - jug1)), # Transfer from jug2 to jug1
            (jug1 - (min(capacity2, jug1 + jug2) - jug2), min(capacity2, jug1 + jug2))  # Transfer from jug1 to jug2
        ]
        
        for state in possible_states:
            if state not in visited:
                queue.append((state, path + [(jug1, jug2)]))
    
    return None  # Return None if no solution is found

def print_solution(path):
    """Print the solution path."""
    if path:
        print("Steps to reach the target:")
        for step in path:
            print(f"Jug1: {step[0]} gallons, Jug2: {step[1]} gallons")
    else:
        print("No solution found.")

def main():
    jug1_capacity = 4  # Capacity of jug1
    jug2_capacity = 3  # Capacity of jug2
    target_amount = 2  # Target amount of water

    # Solve the water jug problem
    solution = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
    
    # Print the solution
    print_solution(solution)
    
    # Print the MAC address
    mac_address = get_mac_address()
    print(f"\nMAC Address: {mac_address}")

if __name__ == "__main__":
    main()

