def dfs(graph, start, goal):
    stack = [(start, [start])] 
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            print("Goal found!")
            print("Path:", path)
            return

        if node not in visited:
            visited.add(node)

            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    print("Goal not found")



graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")


dfs(graph, start, goal)