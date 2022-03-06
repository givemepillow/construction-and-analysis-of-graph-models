from pympler.asizeof import asizeof

from library import AdjacencyMatrix
from .Graph import Graph


class AdjacencyMatrixGraph(Graph):

    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.__str__adjacency_matrix = adjacency_matrix.__str__

    def vertex_neighbors(self, vertex) -> list[str]:
        """
        Находит всех соседей в матрице смежности,
        если вес от заданной вершины к другой вершине или
        наоборот больше нуля. (вес 1 + вес 2 > 0).
        :param vertex: целевая вершина.
        :return: список соседей.
        """
        return [v for v in self.adj_matrix if self.adj_matrix[v][vertex] + self.adj_matrix[vertex][v] > 0]

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        """
        Проверяет, является ли заданная
        последовательность вершин цепью.
        Если нет пути из предыдущей вершины
        к следующей, то заданная последовательность
        вершин цепью не является.
        :param vertexes_sequence: список вершин - цепь.
        :return: True | False.
        """
        for src_vertex, dest_vertex in zip(vertexes_sequence[:-1], vertexes_sequence[1::]):
            if self.adj_matrix[src_vertex][dest_vertex] == 0:
                return False
        return True

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        """
        Список вершин сумма весов чьих инцидентных
        рёбер больше заданного веса.
        Веса для каждой вершины подсчитываются
        с помощью словаря weights_sum,
        где ключом является вершина, а значением сумма весов.
        :param weight: заданный вес.
        :return: список подходящих вершин.
        """
        weights_sum = {}
        for v1 in self.vertexes:
            for v2 in self.vertexes:
                if v1 not in weights_sum:
                    weights_sum[v1] = 0
                weights_sum[v1] += self.adj_matrix[v1][v2] + self.adj_matrix[v2][v1]
        return [v for v in weights_sum if weights_sum[v] > weight]

    def edges_number(self) -> int:
        """
        Подсчитывает количество рёбер путём
        проверки на существование ребра
        между всеми вершинами ([v2][v1] > 0).
        :return: число рёбер
        """
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

    def size(self) -> bytes:
        return asizeof(self.adj_matrix)
