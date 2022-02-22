from library import AdjacencyMatrix
from .Graph import Graph


class AdjacencyMatrixGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.__str__adjacency_matrix = adjacency_matrix.__str__

    def vertex_neighbors(self, vertex) -> list[str]:
        return [v for v in self.adj_matrix if self.adj_matrix[v][vertex] + self.adj_matrix[vertex][v] > 0]

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        for src_vertex, dest_vertex in zip(vertexes_sequence[:-1], vertexes_sequence[1::]):
            if self.adj_matrix[src_vertex][dest_vertex] == 0:
                return False
        return True if len(vertexes_sequence) == len(set(vertexes_sequence)) else False

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        weights_sum = {}
        for v1 in self.vertexes:
            for v2 in self.vertexes:
                if v1 not in weights_sum:
                    weights_sum[v1] = 0
                weights_sum[v1] += self.adj_matrix[v1][v2] + self.adj_matrix[v2][v1]
        return [v for v in weights_sum if weights_sum[v] > weight]

    def edges_number(self) -> list[str]:
        number = 0
        for v1 in self.vertexes:
            for v2 in self.vertexes:
                if self.adj_matrix[v2][v1] > 0:
                    number += 1
        return number

    def render(self, save=False, show=False):
        pass

    def __str__(self):
        return self.__str__adjacency_matrix()
