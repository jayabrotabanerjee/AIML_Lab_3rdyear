from constraint import Problem

def map_coloring():
    # Define the states of Australia and their borders using full names
    states = {
        'Western Australia': [],  # No borders with other states
        'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
        'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
        'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
        'New South Wales': ['South Australia', 'Queensland', 'Victoria'],
        'Victoria': ['South Australia', 'New South Wales'],
        'Tasmania': []  # No borders with other states
    }
    
    # Initialize the problem
    problem = Problem()
    
    # Add variables for each state with a domain of colors 1 through 4
    # You can change the range if more colors are needed
    problem.addVariables(states.keys(), range(1, 5))
    
    # Add constraints that no two adjacent states can have the same color
    for state, neighbors in states.items():
        for neighbor in neighbors:
            problem.addConstraint(lambda s, n: s != n, (state, neighbor))
    
    # Find solutions
    solutions = problem.getSolutions()
    
    if not solutions:
        print("No solution found.")
    else:
        print("Coloring Solution:")
        for sol in solutions:
            for state in states:
                print(f"{state}: Color {sol[state]}")
            break  # Assuming we only need one valid solution

# Run the map coloring function
map_coloring()

