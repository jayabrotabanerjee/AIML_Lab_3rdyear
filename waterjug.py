def print_state(jug1, jug2, jug1_capacity, jug2_capacity):
    print(f"{jug1_capacity}-gallon jug: {jug1} gallons, {jug2_capacity}-gallon jug: {jug2} gallons")

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    # Initial state
    jug1 = 0
    jug2 = 0
    
    steps = []

    # Step 1: Fill the second jug (the one with the smaller capacity)
    jug2 = jug2_capacity
    steps.append(f"Fill {jug2_capacity}-gallon jug: ({jug1}, {jug2})")
    print_state(jug1, jug2, jug1_capacity, jug2_capacity)

    # Step 2: Pour water from the second jug into the first jug
    pour_amount = min(jug2, jug1_capacity - jug1)
    jug1 += pour_amount
    jug2 -= pour_amount
    steps.append(f"Pour from {jug2_capacity}-gallon jug to {jug1_capacity}-gallon jug: ({jug1}, {jug2})")
    print_state(jug1, jug2, jug1_capacity, jug2_capacity)

    # Step 3: Empty the first jug if it is full
    if jug1 == jug1_capacity:
        jug1 = 0
        steps.append(f"Empty {jug1_capacity}-gallon jug: ({jug1}, {jug2})")
        print_state(jug1, jug2, jug1_capacity, jug2_capacity)

    # Step 4: Pour remaining water from the second jug into the first jug
    pour_amount = min(jug2, jug1_capacity - jug1)
    jug1 += pour_amount
    jug2 -= pour_amount
    steps.append(f"Pour remaining {jug2_capacity}-gallon jug into {jug1_capacity}-gallon jug: ({jug1}, {jug2})")
    print_state(jug1, jug2, jug1_capacity, jug2_capacity)

    # Step 5: Fill the second jug again
    jug2 = jug2_capacity
    steps.append(f"Fill {jug2_capacity}-gallon jug: ({jug1}, {jug2})")
    print_state(jug1, jug2, jug1_capacity, jug2_capacity)

    # Step 6: Pour water from the second jug into the first jug
    pour_amount = min(jug2, jug1_capacity - jug1)
    jug1 += pour_amount
    jug2 -= pour_amount
    steps.append(f"Pour from {jug2_capacity}-gallon jug into {jug1_capacity}-gallon jug: ({jug1}, {jug2})")
    print_state(jug1, jug2, jug1_capacity, jug2_capacity)

    # Check if we have achieved the target amount
    if jug1 == target or jug2 == target:
        print(f"Achieved target of {target} gallons in one of the jugs!")
    else:
        print("Failed to achieve target.")

    return steps

def main():
    # User inputs
    jug1_capacity = int(input("Enter the capacity of the first jug (in gallons): "))
    jug2_capacity = int(input("Enter the capacity of the second jug (in gallons): "))
    target = int(input("Enter the target amount of water (in gallons): "))

    if target > max(jug1_capacity, jug2_capacity):
        print("Target exceeds the capacity of the jugs. Exiting.")
        return

    water_jug_problem(jug1_capacity, jug2_capacity, target)

if __name__ == "__main__":
    main()
