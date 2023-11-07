# from itertools import permutations

# def user_input(V: int) -> list:
#     adjacency_matrix = []

#     for _ in range(V):
#         row = input("Enter the row values seperated by spaces: ")
#         row_value = list(map(int, row.split()))
#         adjacency_matrix.append(row_value)

#     print(adjacency_matrix)
#     return adjacency_matrix

# def travelling_salesman(adjacency_matrix: list, cities: list):
#     min_distance = float('inf')
#     shortest_path = None

#     for perm in permutations(cities[1:]):
#         total_distance = 0
#         valid_permutation = True

#         current_city = 'A'
#         for next_city in perm:
#             distance = adjacency_matrix[cities.index(current_city)][cities.index(next_city)]

#             if distance == 0:
#                 valid_permutation = False
#                 break

#             total_distance += distance
#             current_city = next_city
        
#         total_distance += adjacency_matrix[cities.index(current_city)][0]

#         if valid_permutation and total_distance < min_distance:
#             min_distance = total_distance
#             shortest_path = ('A',) + perm + ('A',)
            
#     if shortest_path:
#         print("shortest path: ", shortest_path)
#         print("shortest distance: ", min_distance)
#         return

#     return "No valid path found"

# if __name__ == "__main__":
#     V = int(input("Enter the number of vertices: "))
#     cities = input("Enter cities with spaces: ").split()
#     adjacency_matrix = user_input(V)
#     travelling_salesman(adjacency_matrix, cities)



# import sys

# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for i in range(vertices)] for i in range(vertices)]

#     def add_edge(self, u, v, weight):
#         self.graph[u][v] = weight
#         self.graph[v][u] = weight

#     def prim_mst(self):
#         key = [sys.maxsize] * self.V
#         parent = [None] * self.V
#         key[0] = 0
#         total_cost = 0

#         for _ in range(self.V):
#             u = min((key[i], i) for i in range(self.V) if i not in parent)[1]

#             for v in range(self.V):
#                 if 0 < self.graph[u][v] < key[v] and v not in parent:
#                     key[v] = self.graph[u][v]
#                     parent[v] = u
            
#         for i in range(1, self.V):
#             print(parent[i], i, key[i])
#             total_cost += key[i]
#         print(total_cost)


# if __name__ == "__main__":
#     g = Graph(5)
#     g.add_edge(0, 1, 2)
#     g.add_edge(0, 3, 6)
#     g.add_edge(1, 2, 3)
#     g.add_edge(1, 3, 8)
#     g.add_edge(1, 4, 5)
#     g.add_edge(2, 4, 7)
#     g.add_edge(3, 4, 9)

#     g.prim_mst()

# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
    
#     def add_edge(self, u, v):
#         self.graph[u].append(v)
    
#     def bfs (self, start):
#         visited = set()
#         queue = []

#         queue.append(start)
#         visited.add(start)

#         while queue:
#             current_node = queue.pop(0)
#             print(current_node, end=' ')

#             for neighbor in self.graph[current_node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#                     visited.add(neighbor)
    
#     def dfs (self, start):
#         visited = set()

#         def dfs_util(node):
#             visited.add(node)
#             print(node, end=' ')
            
#             for neighbor in self.graph[node]:
#                 if neighbor not in visited:
#                     dfs_util(neighbor)
        
#         dfs_util(start)


# g = Graph()

# x = int(input("How many edges: "))

# for _ in range (x):
#     e = input("Enter the edges with space: ")
#     edges = list(map(int, e.split()))
#     g.add_edge(edges[0], edges[1])

# # g.add_edge(0, 1)
# # g.add_edge(1, 2)
# # g.add_edge(2, 5)
# # g.add_edge(0, 3)
# # g.add_edge(3, 4)
# # g.add_edge(4, 5)
# # g.add_edge(5, 6)

# print("BFS starting from vertex 0:")
# g.bfs(0)
# print("\nDFS starting from vertex 0:")
# g.dfs(0)

def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, available_colors):
    num_nodes = len(graph)
    colors = [-1] * num_nodes

    def backtrack(node):
        if node == num_nodes:
            return True
        
        for color in available_colors:
            if is_safe(node, color, graph, colors):
                colors[node] = color

                if backtrack(node + 1):
                    return True
                
                colors[node] = None

        return False
    
    if backtrack(0):
        color_mapping = {i: colors[i] for i in range(num_nodes)}
        print(color_mapping)

if __name__ == "__main__":
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2]
    }

    available_colors = ["Red", "Green", "Blue", "Purple", "Gray"]  # Color names as strings

    graph_coloring(graph, available_colors)
