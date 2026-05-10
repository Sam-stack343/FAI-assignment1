# Australia Map Coloring Problem (CSP)

# Regions (variables)
regions = ["WA", "NT", "SA", "QLD", "NSW"]

# Domain (colors)
colors = ["Blue", "Red", "Green"]

# Adjacency constraints (graph)
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "QLD"],
    "SA": ["WA", "NT", "QLD", "NSW"],
    "QLD": ["NT", "SA", "NSW"],
    "NSW": ["SA", "QLD"]
}

# Check if assigning a color is valid
def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking search
def backtrack(assignment):
    # If all regions are assigned, we are done
    if len(assignment) == len(regions):
        return assignment

    # Select unassigned region
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    # Try each color
    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color

            result = backtrack(assignment)
            if result:
                return result

            # Undo assignment (backtrack)
            del assignment[region]

    return None

# Solve the CSP
solution = backtrack({})

# Display result
if solution:
    print("Solution Found:\n")
    for region in regions:
        print(f"{region} = {solution[region]}")
else:
    print("No solution exists.")