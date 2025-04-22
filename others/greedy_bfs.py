def greedy_best_first(graph, start, goal, heuristics, n):
    from heapq import heappush, heappop
    visited = [False] * n
    pq = [(heuristics[start], start, [start])]
    print("Greedy Best-First Path:", end=" ")
    while pq:
        _, node, path = heappop(pq)
        if node == goal:
            print(" -> ".join(map(str, path)))
            return
        if not visited[node]:
            visited[node] = True
            for i in range(n):
                if graph[node][i] == 1 and not visited[i]:
                    heappush(pq, (heuristics[i], i, path + [i]))
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
greedy_best_first(graph, start, goal, heuristics, n)
