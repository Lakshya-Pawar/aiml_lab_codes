def get_neighbors(state, jug1_capacity, jug2_capacity):
    x, y = state
    neighbors = []
    neighbors.append((jug1_capacity, y))
    neighbors.append((x, jug2_capacity))
    neighbors.append((0, y))
    neighbors.append((x, 0))
    if x + y >= jug2_capacity:
        neighbors.append((x - (jug2_capacity - y), jug2_capacity))
    else:
        neighbors.append((0, x + y))
    if x + y >= jug1_capacity:
        neighbors.append((jug1_capacity, y - (jug1_capacity - x)))
    else:
        neighbors.append((x + y, 0))
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx <= jug1_capacity and 0 <= ny <= jug2_capacity]

def heuristic(state, target):
    x, y = state
    return abs(x - target) + abs(y - target)

def hill_climbing(jug1_capacity, jug2_capacity, target):
    current = (0, 0)
    visited = set()
    path = [current]

    while True:
        if current[0] == target or current[1] == target:
            return path
        visited.add(current)
        neighbors = get_neighbors(current, jug1_capacity, jug2_capacity)
        best_neighbor = None
        best_heuristic = float('inf')

        for neighbor in neighbors:
            if neighbor not in visited:
                h = heuristic(neighbor, target)
                if h < best_heuristic:
                    best_heuristic = h
                    best_neighbor = neighbor

        if best_neighbor is None:
            return None
        current = best_neighbor
        path.append(current)

def main():
    jug1_capacity = int(input("Enter capacity of jug 1: "))
    jug2_capacity = int(input("Enter capacity of jug 2: "))
    target = int(input("Enter target amount: "))

    if target > jug1_capacity and target > jug2_capacity:
        print("Target cannot be achieved")
        return

    result = hill_climbing(jug1_capacity, jug2_capacity, target)
    if result:
        print("Solution steps:")
        for i, state in enumerate(result):
            print(f"Step {i}: Jug1 = {state[0]}, Jug2 = {state[1]}")
    else:
        print("No solution found")

main()