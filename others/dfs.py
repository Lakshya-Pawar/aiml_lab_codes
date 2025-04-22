def dfs(graph, node, visited, n):
    print(node, end=" ")
    visited[node] = True
    for i in range(n):
        if graph[node][i] == 1 and not visited[i]:
            dfs(graph, i, visited, n)

n = int(input("Nodes: "))
print("Enter matrix (0/1, row by row):")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
start = int(input("Start node: "))
visited = [False] * n
print("DFS:", end=" ")
dfs(graph, start, visited, n)
print()
