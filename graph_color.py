def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, available_colors):
    num_nodes = len(graph)
    colors = [-1] * num_nodes  # Initialize all nodes with no color

    def backtrack(node):
        if node == num_nodes:
            return True  # All nodes are colored

        for color in available_colors:
            if is_safe(node, color, graph, colors):
                colors[node] = color

                # Recursively color the next node
                if backtrack(node + 1):
                    return True

                # If coloring the next node doesn't lead to a solution, backtrack
                colors[node] = None

        return False  # No valid color for the current node

    if backtrack(0):
        color_mapping = {i: colors[i] for i in range(num_nodes)}
        print("Solution found! Node colors:", color_mapping)
    else:
        print("No solution exists with the given colors.")

# Example usage:
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2]
    }

    available_colors = ["Red", "Green", "Blue", "Purple", "Gray"]  # Color names as strings

    graph_coloring(graph, available_colors)
