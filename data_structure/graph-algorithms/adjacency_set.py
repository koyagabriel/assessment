import numpy as np
from graph import Graph

# A single node is a graph represented by an adjacency set. 
# Every node has a vertex Id. 
# Each node is associated with a set of adjacent vertices

class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacent_set = set()
    
    def add_edge(self, v):
        if self.vertex_id == v: raise ValueError(f'The vertex {v} cannot be adjacent to itself')
        
        self.adjacent_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacent_set)


class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')

        if weight != 1:
            raise ValueError('An adjacency set cannot represent edge weights > 1' )

        self.vertex_list[v1].add_edge(v2)

        not self.directed and self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')

        return self.vertex_list[v].get_adjacent_vertices() 

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')

        indegree = 0
        for i in range(self.num_vertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(f'{i}, -->, {v}')


                
g = AdjacencySetGraph(4)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

for i in range(4):
    print(f'Adjacent to: {i}, {g.get_adjacent_vertices(i)}')

for i in range(4):
    print(f'Indegree: {i}, {g.get_indegree(i)}')

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print(f'Edge weight: {i}, , {j}, weight:, {g.get_edge_weight(i, j)}')

g.display()