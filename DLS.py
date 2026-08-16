graph = 
{
    "START": ["A", "B"],
    "A": ["C"],
    "B": ["D"],
    "C": ["GOAL"],
    "D": [],
    "GOAL": []
}

def dls(node, goal, limit):

    if node == goal:
        return [node]

    if limit == 0:
        return None

    for neighbour in graph[node]:

        path = dls(neighbour, goal, limit - 1)

        if path:
            return [node] + path

    return None


limit = 3

path = dls("START", "GOAL", limit)

print("Depth Limited Search:")

if path:
    print(" → ".join(path))
else:
    print("Goal not found within depth limit")
