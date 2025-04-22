def a_star(graph, start, goal, heuristics, n):
    from heapq import heappush, heappop
    visited = [False] * n
    pq = [(heuristics[start], 0, start, [start])]
    print("A* Path:", end=" ")
    while pq:
        _, cost, node, path = heappop(pq)
        if node == goal:
            print(" -> ".join(map(str, path)))
            return
        if not visited[node]:
            visited[node] = True
            for i in range(n):
                if graph[node][i] == 1 and not visited[i]:
                    g = cost + 1
                    f = g + heuristics[i]
                    heappush(pq, (f, g, i, path + [i]))
    print("No path found")

n = int(input("Nodes: "))
print("Enter matrix (0/1, row by row):")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
start = int(input("Start node: "))
heuristics = list(map(int, input("Heuristics for each node: ").split()))
goal = int(input("Goal node: "))
a_star(graph, start, goal, heuristics, n)
