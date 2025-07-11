def min_max(game_tree, node, is_max):
    # If the node is a leaf (contains a numeric value), return it
    if isinstance(node, int):
        return node

    # If the node has no children, return it directly (should not happen here)
    if not game_tree.get(node):
        return node

    if is_max:
        best_value = float('-inf')
        for child in game_tree[node]:
            value = min_max(game_tree, child, False)
            best_value = max(best_value, value)
    else:
        best_value = float('inf')
        for child in game_tree[node]:
            value = min_max(game_tree, child, True)
            best_value = min(best_value, value)

    return best_value

# Game tree with numeric leaf values
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3],
    'E': [5],
    'F': [6],
    'G': [9]
}

print(min_max(game_tree, 'A', True))
