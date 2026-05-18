from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:

        current_node, path = queue.popleft()

        if current_node == goal:
            print("Goal Found!")
            print("Search Path:", " -> ".join(path))
            return

        visited.add(current_node)

        for neighbor in graph[current_node]:

            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    print("Goal node not found.")

start_node = 'A'
goal_node = 'G'

print("BREADTH FIRST SEARCH")
bfs(graph, start_node, goal_node)