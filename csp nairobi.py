# Nairobi Constituencies CSP
# Map Coloring Problem

constituencies = [
    "Westlands", "Dagoretti_North", "Dagoretti_South", "Langata",
    "Kibra", "Roysambu", "Kasarani", "Ruaraka",
    "Embakasi_North", "Embakasi_South", "Embakasi_Central",
    "Embakasi_East", "Embakasi_West", "Makadara",
    "Kamukunji", "Starehe", "Mathare"
]


colors = ["Blue", "Red", "Green"]




neighbors = {
    "Westlands": ["Dagoretti_North", "Kibra", "Mathare", "Starehe"],
    "Dagoretti_North": ["Westlands", "Dagoretti_South", "Kibra"],
    "Dagoretti_South": ["Dagoretti_North", "Langata", "Kibra"],
    "Langata": ["Dagoretti_South", "Kibra", "Embakasi_South"],
    "Kibra": ["Westlands", "Dagoretti_North", "Dagoretti_South", "Langata"],

    "Roysambu": ["Kasarani", "Ruaraka", "Mathare"],
    "Kasarani": ["Roysambu", "Ruaraka", "Embakasi_East"],
    "Ruaraka": ["Roysambu", "Kasarani", "Mathare"],

    "Embakasi_North": ["Embakasi_East", "Ruaraka"],
    "Embakasi_South": ["Langata", "Makadara", "Embakasi_Central"],
    "Embakasi_Central": ["Embakasi_South", "Embakasi_West", "Embakasi_East"],
    "Embakasi_East": ["Kasarani", "Embakasi_Central", "Embakasi_North"],
    "Embakasi_West": ["Embakasi_Central", "Starehe"],

    "Makadara": ["Embakasi_South", "Kamukunji", "Starehe"],
    "Kamukunji": ["Makadara", "Starehe", "Mathare"],
    "Starehe": ["Westlands", "Makadara", "Kamukunji", "Embakasi_West"],
    "Mathare": ["Westlands", "Roysambu", "Ruaraka", "Kamukunji"]
}



def is_valid(node, color, assignment):
    for neighbor in neighbors[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True





def backtrack(assignment):
    if len(assignment) == len(constituencies):
        return assignment

    unassigned = [c for c in constituencies if c not in assignment]
    node = unassigned[0]

    for color in colors:
        if is_valid(node, color, assignment):
            assignment[node] = color

            result = backtrack(assignment)
            if result:
                return result

            del assignment[node]

    return None




solution = backtrack({})


if solution:
    print("\nSolution using 3 colors:\n")
    for c in constituencies:
        print(f"{c}: {solution[c]}")
else:
    print("\nNo solution with 3 colors. Trying 4 colors...\n")

    colors = ["Blue", "Red", "Green", "Yellow"]
    solution = backtrack({})

    if solution:
        print("Solution using 4 colors:\n")
        for c in constituencies:
            print(f"{c}: {solution[c]}")
    else:
        print("No solution found even with 4 colors.")