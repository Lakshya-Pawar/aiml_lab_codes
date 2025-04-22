def tsp_dfs(graph, start):
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    path = [start]
    min_cost = float('inf')
    best_path = []

    def dfs(curr, cost, count):
        nonlocal min_cost, best_path
        if count == n:
            if graph[curr][start] != 0:
                total_cost = cost + graph[curr][start]
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = path[:]
                    best_path.append(start)
            return

        for next_city in range(n):
            if not visited[next_city] and graph[curr][next_city] != 0:
                visited[next_city] = True
                path.append(next_city)
                dfs(next_city, cost + graph[curr][next_city], count + 1)
                visited[next_city] = False
                path.pop()

    dfs(start, 0, 1)
    return best_path, min_cost

def tsp_bfs(graph, start):
    from collections import deque
    n = len(graph)
    min_cost = float('inf')
    best_path = []
    queue = deque([(start, [start], 0, {start})])

    while queue:
        curr, path, cost, visited = queue.popleft()
        if len(path) == n:
            if graph[curr][start] != 0:
                total_cost = cost + graph[curr][start]
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = path[:] + [start]
            continue

        for next_city in range(n):
            if next_city not in visited and graph[curr][next_city] != 0:
                new_visited = visited | {next_city}
                queue.append((next_city, path + [next_city], cost + graph[curr][next_city], new_visited))

    return best_path, min_cost

def get_user_graph():
    n = int(input("Enter number of cities: "))
    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            else:
                cost = int(input(f"Enter cost from city {i} to city {j} (0 if no path): "))
                row.append(cost)
        graph.append(row)
    return graph

def main():
    graph = get_user_graph()
    start_city = int(input("Enter starting city (0 to {}): ".format(len(graph)-1)))
    dfs_path, dfs_cost = tsp_dfs(graph, start_city)
    bfs_path, bfs_cost = tsp_bfs(graph, start_city)
    print(f"DFS Path: {dfs_path}, Cost: {dfs_cost}")
    print(f"BFS Path: {bfs_path}, Cost: {bfs_cost}")

main()