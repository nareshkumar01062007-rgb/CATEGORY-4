graph = 
{
    "START": ["A", "B"],
    "A": ["C"],
    "B": ["D"],
    "C": [],
    "D": ["GOAL"],
    "GOAL": []
}

def dfs(node, goal, visited):

    if node == goal:
        return [node]

    visited.add(node)

    for neighbour in graph[node]:

        if neighbour not in visited:

            path = dfs(neighbour, goal, visited)

            if path:
                return [node] + path

    return None


path = dfs("START", "GOAL", set())

print("DFS Path:")
print(" → ".join(path))
