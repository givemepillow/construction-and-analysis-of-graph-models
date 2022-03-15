from pympler.asizeof import asizeof

from texttable import Texttable

from library import AdjacencyMatrix
from library.types import Record
from .Graph import Graph


class RecordsArrayGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.records = {}
        for vertex in self.vertexes:
            out_edges_weight, in_edges_weight = [], []
            parents, children = [], []
            for child, weight in self.adj_matrix[vertex].items():
                if weight > 0:
                    out_edges_weight.append(weight)
                    children.append(child)
            for parent in self.adj_matrix[vertex]:
                if self.adj_matrix[parent][vertex] > 0:
                    in_edges_weight.append(self.adj_matrix[parent][vertex])
                    parents.append(parent)

            self.records[vertex] = Record(
                vertex=vertex,
                vertex_number=self.vertexes[vertex],
                parents=parents,
                children=children,
                out_edges_weight=out_edges_weight,
                in_edges_weight=in_edges_weight
            )

    def vertex_neighbors(self, vertex) -> list[str]:
        """
        Возвращает соседей указанной вершины из списка записей.
        :param vertex: целевая вершина.
        :return: список соседей.
        """
        return self.records[vertex].neighbors if vertex in self.records else []

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        """
        Проверяет, является ли заданная
        последовательность вершин цепью.
        Если следующая вершина
        не является потомком предыдущей,
        то заданная последовательность
        вершин цепью не является.
        :param vertexes_sequence: список вершин - цепь.
        :return: True | False.
        """
        for src_vertex, dest_vertex in zip(vertexes_sequence[:-1], vertexes_sequence[1::]):
            if dest_vertex not in self.records[src_vertex].children:
                return False
        return True

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        """
        Список вершин сумма весов чьих
        инцидентных рёбер больше заданного веса.
        Веса для каждой вершины подсчитываются
        суммированием весов инцидентных рёбер.
        :param weight: заданный вес.
        :return: список подходящих вершин.
        """
        return [r.vertex for r in self.records.values() if sum(r.incident_edges_weight) > weight]

    def edges_number(self) -> int:
        """
        Подсчитывает количество рёбер путём
        подсчёта количества детей для каждой вершины.
        :return: число рёбер
        """
        return sum((len(r.children) for r in self.records.values()))

    def max_min_vertex(self):
        max_vertex = None
        max_number = 0
        for r in self.records.values():
            if len(r.neighbors) > max_number:
                max_vertex = r.vertex
                max_number = len(r.neighbors)
        min_number = max_number
        result = []
        for v in self.records[max_vertex].neighbors:
            if len(self.records[v].neighbors) < min_number:
                min_number = len(self.records[v].neighbors)
                result.clear()
                result.append(v)
            elif len(self.records[v].neighbors) == min_number:
                result.append(v)
        return result

    def size(self) -> bytes:
        return asizeof(self.records)

    def render(self, save=False, show=False):
        pass

    def __str__(self) -> str:
        table = Texttable()
        table.set_cols_align(["c", "c", "r", "l", "r", "l"])
        rows = [['№', 'Vertex', 'Parents', 'Children', "In weights", "Out weights"]]
        for r in self.records.values():
            rows.append([
                r.vertex_number,
                r.vertex,
                r.parents,
                r.children,
                r.in_edges_weight,
                r.out_edges_weight

            ])
        return str(table.add_rows(rows).draw())
