from abc import ABC, abstractmethod


from library.AdjacencyMatrix import AdjacencyMatrix


class Graph(ABC):
    @abstractmethod
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        self.adj_matrix = adjacency_matrix.get_adjacency_matrix()
        self.vertexes = {}
        for i, v in enumerate(self.adj_matrix):
            self.vertexes[v] = i + 1

    @abstractmethod
    def vertex_neighbors(self, vertex_name) -> list[str]:
        pass

    @abstractmethod
    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        pass

    @abstractmethod
    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        pass

    @abstractmethod
    def edges_number(self) -> list[str]:
        pass

    @abstractmethod
    def render(self, save=False, show=False):
        pass
