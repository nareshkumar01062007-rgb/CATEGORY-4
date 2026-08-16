graph = 
{
    "Chennai": ["A"],
    "A": ["B"],
    "B": ["C"],
    "C": ["Bangalore"],
    "Bangalore": []
}

reverse_graph =
{
    "Bangalore": ["C"],
    "C": ["B"],
    "B": ["A"],
    "A": ["Chennai"],
    "Chennai": []
}

def bfs(start, goal, graph):

    queue = [[start]]
    visited = set()

    while queue:

        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:

            visited.add(node)

            for neighbour in graph[node]:
                queue.append(path + [neighbour])

    return None


start = "Chennai"
goal = "Bangalore"

forward = bfs(start, goal, graph)
backward = bfs(goal, start, reverse_graph)

print("Bidirectional Search:")

print("From Start:")
print(" → ".join(forward))

print("From Goal:")
print(" → ".join(backward))
