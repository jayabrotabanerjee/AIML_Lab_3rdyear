from constraint import Problem, AllDifferentConstraint

def get_user_input():
    # Input for the cryptarithm equation
    equation = input("Enter the cryptarithm equation (e.g., LEAD + BEAD = READ): ").strip().upper()
    
    # Parse the equation
    try:
        left_side, result = equation.split('=')
        left_terms = left_side.split('+')
        result = result.strip()
        left_terms = [term.strip() for term in left_terms]
        result = result.strip()
    except ValueError:
        raise ValueError("Invalid format. Make sure to use the format 'TERM1 + TERM2 = RESULT'.")
    
    # Collect all unique letters
    terms = left_terms + [result]
    letters = set(''.join(terms))
    
    return letters, left_terms, result

def cryptarithm_constraint(letters, *args):
    # Create a dictionary to map letters to their corresponding digits
    letter_to_digit = {letter: digit for letter, digit in zip(letters, args)}
    
    def calculate_term(term):
        return sum(letter_to_digit[char] * 10**i for i, char in enumerate(reversed(term)))
    
    # Calculate the sum of left terms
    left_sum = sum(calculate_term(term) for term in left_terms)
    
    # Calculate the result term
    result_value = calculate_term(result)
    
    return left_sum == result_value

def main():
    # Get user input
    global left_terms, result
    letters, left_terms, result = get_user_input()
    
    # Ensure all letters are unique
    if len(letters) > 10:
        raise ValueError("Too many unique letters. Each letter must be assigned a unique digit from 0-9.")

    # Create a problem instance
    problem = Problem()
    
    # Define digits range
    digits = range(10)
    
    # Add variables to the problem
    for letter in letters:
        problem.addVariable(letter, digits)

    # Add constraint for all variables to be different
    problem.addConstraint(AllDifferentConstraint())

    # Define the constraint dynamically
    problem.addConstraint(lambda *args: cryptarithm_constraint(letters, *args), letters)
    
    # Solve the problem
    solutions = problem.getSolutions()

    # Print the solutions
    if solutions:
        for solution in solutions:
            # Display the solution
            print("Solution:")
            for letter in letters:
                print(f"{letter} = {solution[letter]}")
            # Optionally, compute and display the equation
            def calculate_term(term):
                return sum(solution[char] * 10**i for i, char in enumerate(reversed(term)))
            
            print(f"{' + '.join(left_terms)} = {result}")
            print(f"Evaluated: {sum(calculate_term(term) for term in left_terms)} = {calculate_term(result)}")
    else:
        print("No solution found")

if __name__ == "__main__":
    main()

