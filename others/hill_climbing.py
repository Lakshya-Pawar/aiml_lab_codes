def hill_climbing(graph, start, goal, heuristics, n):
    current = start
    path = [start]
    print("Hill Climbing Path:", end=" ")
    while current != goal:
        neighbors = [i for i in range(n) if graph[current][i] == 1]
        if not neighbors:
            print("No path found")
            return
        next_node = min(neighbors, key=lambda x: heuristics[x])
        if heuristics[next_node] >= heuristics[current]:
            print(" -> ".join(map(str, path)))
            return
        current = next_node
        path.append(current)
    print(" -> ".join(map(str, path)))

n = int(input("Nodes: "))
print("Enter matrix (0/1, row by row):")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
start = int(input("Start node: "))
heuristics = list(map(int, input("Heuristics for each node: ").split()))
goal = int(input("Goal node: "))
hill_climbing(graph, start, goal, heuristics, n)
