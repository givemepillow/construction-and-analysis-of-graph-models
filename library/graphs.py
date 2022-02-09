from abc import ABC, abstractmethod
from unittest import result
from library.types import Edge, Vertex
from library.adjacency_matrix import AdjacencyMatrix

class Graph(ABC):
    @abstractmethod
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        pass

    @abstractmethod
    def render(self):
        pass

class EdgesListGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.__adjacency_matrix = adjacency_matrix.get_adjanceny_matrix()
        matrix = self.__adjacency_matrix
        self.edges = [
            Edge(out_vertex=v1,in_vertex=v2, weight=matrix[v1][v2]) 
            for v1 in matrix for v2 in matrix[v1] if matrix[v1][v2] > 0
        ]

    def render(self):
        pass
    
    def __str__(self):
        return '\n'.join(map(str, self.edges))
        


class AdjacencyMatrixGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.__adjacency_matrix = adjacency_matrix.get_adjanceny_matrix()

    def render(self):
        pass

class RecordsArrayGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.__adjacency_matrix = adjacency_matrix.get_adjanceny_matrix()

    def render(self):
        pass

