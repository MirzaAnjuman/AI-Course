def alpha_beta(game_tree, node, is_max, alpha, beta):
    # If the node is a leaf (integer), return it
    if isinstance(node, int):
        return node

    # If the node has no children, return the node itself (should not happen here)
    if not game_tree.get(node):
        return node

    if is_max:
        best_value = float('-inf')
        for child in game_tree[node]:
            value = alpha_beta(game_tree, child, False, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if beta <= alpha:
                break  # Beta cut-off
        return best_value

    else:
        best_value = float('inf')
        for child in game_tree[node]:
            value = alpha_beta(game_tree, child, True, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if beta <= alpha:
                break  # Alpha cut-off
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

# Run alpha-beta pruning from root
print(alpha_beta(game_tree, 'A', True, float('-inf'), float('inf')))
