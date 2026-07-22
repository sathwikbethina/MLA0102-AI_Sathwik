graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

def best_first(start, goal):
    path = [start]

    while start != goal:
        if not graph[start]:
            return "Path not found"

        next_node = min(graph[start], key=lambda x: heuristic[x])
        path.append(next_node)
        start = next_node

    return path

result = best_first('A', 'G')
print("Path:", " -> ".join(result))