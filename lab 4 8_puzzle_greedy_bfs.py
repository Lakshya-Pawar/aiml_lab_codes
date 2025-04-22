def get_manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                value = state[i][j]
                for gi in range(3):
                    for gj in range(3):
                        if goal[gi][gj] == value:
                            distance += abs(i - gi) + abs(j - gj)
    return distance

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def greedy_best_first_search(initial, goal):
    from heapq import heappush, heappop
    visited = set()
    pq = [(get_manhattan_distance(initial, goal), initial, [initial])]

    while pq:
        _, current, path = heappop(pq)
        current_tuple = tuple(tuple(row) for row in current)
        if current == goal:
            return path
        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple not in visited:
                heappush(pq, (get_manhattan_distance(neighbor, goal), neighbor, path + [neighbor]))

    return None

def print_state(state):
    for row in state:
        print(row)
    print()

def main():
    print("Enter initial state (3x3, use 0 for blank, row by row):")
    initial = []
    for _ in range(3):
        row = list(map(int, input().split()))
        initial.append(row)

    print("Enter goal state (3x3, use 0 for blank, row by row):")
    goal = []
    for _ in range(3):
        row = list(map(int, input().split()))
        goal.append(row)

    result = greedy_best_first_search(initial, goal)
    if result:
        print("Solution steps:")
        for i, state in enumerate(result):
            print(f"Step {i}:")
            print_state(state)
    else:
        print("No solution found")

main()