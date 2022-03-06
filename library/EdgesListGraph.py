import networkx as nx
import matplotlib.pyplot as plt
from pympler.asizeof import asizeof
from texttable import Texttable

from library import AdjacencyMatrix
from library.types import Edge
from .Graph import Graph


class EdgesListGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        matrix = self.adj_matrix
        self.edges = [
            Edge(scr_vertex=v1, dest_vertex=v2, weight=matrix[v1][v2])
            for v1 in matrix for v2 in matrix[v1] if matrix[v1][v2] > 0
        ]

    def vertex_neighbors(self, vertex) -> list[str]:
        """
        Находит всех соседей в списке смежности,
        если заданная вершина
        является родителем или потомком.
        :param vertex: целевая вершина.
        :return: список соседей.
        """
        neighbors = []
        for edge in self.edges:
            if vertex in (edge.dest_vertex, edge.scr_vertex):
                neighbors.append(edge.dest_vertex if edge.dest_vertex != vertex else edge.scr_vertex)
        return neighbors

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        """
        Проверяет, является ли заданная последовательность
        вершин цепью. Если нет пути из предыдущей вершины
        к следующей, то заданная последовательность
        вершин цепью не является.
        :param vertexes_sequence: список вершин - цепь.
        :return: True | False.
        """
        for src_vertex, dest_vertex in zip(vertexes_sequence[:-1], vertexes_sequence[1::]):
            flag = True
            for edge in self.edges:
                if edge.scr_vertex == src_vertex and edge.dest_vertex == dest_vertex:
                    flag = False
                    break
            if flag:
                return False
        return True

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        """
        Список вершин сумма весов чьих инцидентных
        рёбер больше заданного веса.
        Веса для каждой вершины подсчитываются
        с помощью словаря weights_sum,
        где ключом является вершина,
        а значением сумма весов.
        Ребро находится путём проверки на то
        является ли выбранная вершина инцидентной ребру.
        (if v in (edge.dest_vertex, edge.scr_vertex))
        :param weight: заданный вес.
        :return: список подходящих вершин.
        """
        weights_sum = {}
        for v in self.vertexes:
            for edge in self.edges:
                if v in (edge.dest_vertex, edge.scr_vertex):
                    weights_sum[v] = (edge.weight + weights_sum[v]) if v in weights_sum else edge.weight
        return [v for v in weights_sum if weights_sum[v] > weight]

    def edges_number(self) -> int:
        """
        Подсчитывает количество рёбер путём
        нахождения длины списка рёбер.
        :return: число рёбер
        """
        return len(self.edges)

    def size(self) -> bytes:
        return asizeof(self.edges)

    def render(self, save=False, show=False):
        graph = nx.DiGraph()
        graph.add_nodes_from([v for v in self.vertexes])
        for e in self.edges:
            graph.add_edge(e.scr_vertex, e.dest_vertex, weight=e.weight)
        plt.figure(figsize=(5, 5), dpi=200)
        pos = nx.planar_layout(graph)
        nx.draw(graph,
                pos=pos,
                node_color='lightgreen',
                node_size=700,
                with_labels=True,
                font_size=15,
                arrowsize=5
                )
        nx.draw_networkx_edge_labels(
            graph, pos, edge_labels={(e.scr_vertex, e.dest_vertex): e.weight for e in self.edges},
            font_color='purple',
            font_size=15
        )
        if save:
            plt.savefig("graph.png", format="PNG")
        if show:
            plt.show()

    def __str__(self):
        table = Texttable()
        table.set_cols_align(["c", "c"])
        rows = [['Edge', 'Weight']]
        for edge in self.edges:
            rows.append([f"{edge.scr_vertex} -> {edge.dest_vertex}", f"{edge.weight}"])
        table.add_rows(rows)
        return str(table.draw())
