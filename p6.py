from collections import deque

def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Initialize queue with the starting node
    
    while queue:
        node = queue.popleft()   # Remove from front of the queue
        if node not in visited:
            print(node, end=" ") # Process the node (here we just print it)
            visited.add(node)
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS Traversal starting from node A:")
bfs(graph, 'A')
