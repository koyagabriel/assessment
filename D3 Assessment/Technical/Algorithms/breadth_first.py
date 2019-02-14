import numpy as np
from queue import Queue
from adjacency_matrix import AdjacencyMatrixGraph


def breadth_first(graph: AdjacencyMatrixGraph, target_number, start_node: int = 0):
    queue: Queue = Queue()
    queue.put(start_node)

    visited: np.ndarray = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex: int = queue.get()
        if visited[vertex]:
            continue
        print(f'Visit --> {vertex}')
        visited[vertex] = True

        for v in graph.get_adjacent_vertices(vertex):
            not(visited[v]) and queue.put(v)

if __name__ == '__main__':
    g = AdjacencyMatrixGraph(9)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2 ,7)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 3)
    g.add_edge(3, 4)
    g.add_edge(6, 8)


    breadth_first(g, 0)
