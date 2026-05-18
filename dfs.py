graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

def dfs(graph, current_node, goal, visited=None, path=None):

    if visited is None:
        visited = set()

    if path is None:
        path = []

    visited.add(current_node)

    path.append(current_node)

    if current_node == goal:
        print("Goal Found!")
        print("Search Path:", " -> ".join(path))
        return True

    for neighbor in graph[current_node]:

        if neighbor not in visited:

            if dfs(graph, neighbor, goal, visited, path):
                return True

    path.pop()

    return False

start_node = 'A'
goal_node = 'G'

print("DEPTH FIRST SEARCH")
dfs(graph, start_node, goal_node)