def bfs(graph, start, n):
    visited = [False] * n
    queue = [start]
    visited[start] = True
    print("BFS:", end=" ")
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
    print()

n = int(input("Nodes: "))
print("Enter matrix (0/1, row by row):")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
start = int(input("Start node: "))
bfs(graph, start, n)
