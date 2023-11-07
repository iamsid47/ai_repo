from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = []

        queue.append(start)
        visited.add(start)

        while queue:
            current_node = queue.pop(0)
            print(current_node, end=' ')

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    
    def dfs(self, start):
        visited = set()

        def dfs_util(node):
            visited.add(node)
            print(node, end=' ')

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)

# Example usage:
g = Graph()

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 5)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)

print("BFS starting from vertex 0:")
g.bfs(0)
print("\nDFS starting from vertex 0:")
g.dfs(0)
