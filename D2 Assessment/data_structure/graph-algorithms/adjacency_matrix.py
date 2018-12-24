import numpy as np
from graph import Graph

class AdjacencyMatrixGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')
                   
        if weight < 1: raise ValueError('An edge cannot have weight < 1')

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices: raise ValueError(f'Cannot access vertex {v}')

        adjacent_vertices = []
        for i in range(self.numVertices):
            self.matrix[v][i] > 0 and adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        # for indegree, the weight value must be positive
        if (v < 0 or v >= self.numVertices):raise ValueError(f'cannot access vertex {v}')

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return  self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(f'{i}, -->, {v}')



g = AdjacencyMatrixGraph(4)

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