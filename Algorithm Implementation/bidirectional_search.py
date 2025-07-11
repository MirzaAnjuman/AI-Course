from collections import deque

# Undirected graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Queues for forward and backward search
    forward_queue = deque([(start, [start])])
    backward_queue = deque([(goal, [goal])])

    # Visited dictionaries to store paths
    forward_visited = {start: [start]}
    backward_visited = {goal: [goal]}

    while forward_queue and backward_queue:
        # Expand forward search
        node_f, path_f = forward_queue.popleft()
        if node_f in backward_visited:
            return path_f + backward_visited[node_f][-2::-1]

        for neighbor in graph.get(node_f, []):
            if neighbor not in forward_visited:
                new_path = path_f + [neighbor]
                forward_visited[neighbor] = new_path
                forward_queue.append((neighbor, new_path))

        # Expand backward search
        node_b, path_b = backward_queue.popleft()
        if node_b in forward_visited:
            return forward_visited[node_b] + path_b[-2::-1]

        for neighbor in graph.get(node_b, []):
            if neighbor not in backward_visited:
                new_path = path_b + [neighbor]
                backward_visited[neighbor] = new_path
                backward_queue.append((neighbor, new_path))

    # No connection found
    return None

# Test the function
print(bidirectional_search(graph, 'A', 'F'))
