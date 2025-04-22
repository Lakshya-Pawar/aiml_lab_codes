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

def a_star(jug1_capacity, jug2_capacity, target):
    from heapq import heappush, heappop
    open_list = [(0, 0, (0, 0), [(0, 0)])]
    visited = set()

    while open_list:
        f, g, state, path = heappop(open_list)
        if state[0] == target or state[1] == target:
            return path
        state_tuple = tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for neighbor in get_neighbors(state, jug1_capacity, jug2_capacity):
            if tuple(neighbor) not in visited:
                g_new = g + 1
                h = heuristic(neighbor, target)
                f_new = g_new + h
                heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None

def main():
    jug1_capacity = int(input("Enter capacity of jug 1: "))
    jug2_capacity = int(input("Enter capacity of jug 2: "))
    target = int(input("Enter target amount: "))

    if target > jug1_capacity and target > jug2_capacity:
        print("Target cannot be achieved")
        return

    result = a_star(jug1_capacity, jug2_capacity, target)
    if result:
        print("Solution steps:")
        for i, state in enumerate(result):
            print(f"Step {i}: Jug1 = {state[0]}, Jug2 = {state[1]}")
    else:
        print("No solution found")

main()