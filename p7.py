def iddfs(graph, start, goal, max_depth):
    for depth_limit in range(max_depth + 1):
        stack = [(start, 0, [start])]

        while stack:
            node, depth, path = stack.pop()

            if node == goal:
                print("Goal found at depth", depth)
                print("Path:", path)
                return

            if depth < depth_limit:
                for neighbor in reversed(graph.get(node, [])):
                    if neighbor not in path:
                        stack.append((neighbor, depth + 1, path + [neighbor]))

    print("Goal not found")


# ---- User Input Section ----
graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter max depth: "))

# Run IDDFS
iddfs(graph, start, goal, max_depth)