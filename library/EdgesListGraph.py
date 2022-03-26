import networkx as nx
import matplotlib.pyplot as plt
from pympler.asizeof import asizeof
from texttable import Texttable

from .AdjacencyMatrix import AdjacencyMatrix
from .types import Edge
from .Graph import Graph


class EdgesListGraphOnEdges:
    def __init__(self, edges: list[Edge]):
        self.vertexes = {}
        self.edges = edges
        i = 0
        for e in edges:
            self.vertexes[e.scr_vertex] = i
            self.vertexes[e.dest_vertex] = i

    def vertex_neighbors(self, vertex_name) -> list[str]:
        return EdgesListGraph.vertex_neighbors(self, vertex_name)

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        return EdgesListGraph.is_chain(self, vertexes_sequence)

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        return EdgesListGraph.vertex_by_weights_sum(self, weight)

    def edges_number(self) -> int:
        return EdgesListGraph.edges_number(self)

    def size(self) -> bytes:
        return EdgesListGraph.size(self)

    @property
    def weights_sum(self):
        return sum([e.weight for e in self.edges])

    def render(self, save=False, show=False, planar=True, highlights=None):
        return EdgesListGraph.render(self, save, show, planar, highlights)

    def __str__(self):
        return EdgesListGraph.__str__(self)


class EdgesListGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        matrix = self.adj_matrix
        self._edges = [
            Edge(scr_vertex=v1, dest_vertex=v2, weight=matrix[v1][v2])
            for v1 in matrix for v2 in matrix[v1] if matrix[v1][v2] > 0
        ]

    @property
    def edges(self):
        return set(self._edges)

    def mst(self, start_node=None) -> EdgesListGraphOnEdges:
        """
        Реализация алгоритма Прима. Здесь используется множество
        вершин дерева (mst_vertexes), пополняемое в ходе составления
        mst-дерева. _edges - множество всех рёбер, из которых
        выбирается минимальное при составлении mst-дерева
        (min(_edges, key=lambda edge: edge.weight)). Ребро является
        подходящим тогда и только тогда, когда одна из его вершин
        уже находится в дереве, а вторая ещё нет
        (in mst_vertexes and e.dest_vertex not in mst_vertexes).
        :return: EdgesListGraphOnEdges - минимальное остовное дерево графа.
        """
        if start_node:
            mst_vertexes = {start_node}
        else:
            mst_vertexes = {tuple(self.vertexes)[0]}
        _edges = set(self._edges)
        while len(mst_vertexes) != len(self.vertexes):
            edges = [e for e in _edges if e.scr_vertex in mst_vertexes and e.dest_vertex not in mst_vertexes]
            if not edges:
                break
            min_edge = min(edges, key=lambda edge: edge.weight)
            _edges.discard(min_edge)
            mst_vertexes |= {min_edge.scr_vertex, min_edge.dest_vertex}
        return EdgesListGraphOnEdges(set(self._edges) - _edges)

    def vertex_neighbors(self, vertex) -> list[str]:
        """
        Находит всех соседей в списке смежности,
        если заданная вершина
        является родителем или потомком.
        :param vertex: целевая вершина.
        :return: список соседей.
        """
        neighbors = []
        for edge in self._edges:
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
            for edge in self._edges:
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
            for edge in self._edges:
                if v in (edge.dest_vertex, edge.scr_vertex):
                    weights_sum[v] = (edge.weight + weights_sum[v]) if v in weights_sum else edge.weight
        return [v for v in weights_sum if weights_sum[v] > weight]

    def edges_number(self) -> int:
        """
        Подсчитывает количество рёбер путём
        нахождения длины списка рёбер.
        :return: число рёбер
        """
        return len(self._edges)

    def size(self) -> bytes:
        return asizeof(self._edges)

    def render(self, save=False, show=False, planar=True, highlights=None):
        graph = nx.DiGraph()
        graph.add_nodes_from([v for v in self.vertexes])
        colors = []
        for e in self._edges:
            if highlights:
                _e = Edge(scr_vertex=e.dest_vertex, dest_vertex=e.scr_vertex, weight=e.weight)
                graph.add_edge(e.scr_vertex, e.dest_vertex, weight=e.weight)
                colors.append('orange' if e in highlights or _e in highlights else 'deepskyblue')
            else:
                graph.add_edge(e.scr_vertex, e.dest_vertex, weight=e.weight)
                colors.append('deepskyblue')

        plt.figure(figsize=(5, 5), dpi=200)
        if planar:
            pos = nx.planar_layout(graph)
        else:
            pos = nx.spring_layout(graph)

        nx.draw(graph,
                pos=pos,
                node_color='lightgreen',
                node_size=300,
                with_labels=True,
                font_size=10,
                arrowsize=5,
                edge_color=colors
                )
        nx.draw_networkx_edge_labels(
            graph, pos, edge_labels={(e.scr_vertex, e.dest_vertex): e.weight for e in self._edges},
            font_color='purple',
            font_size=8
        )
        if save:
            plt.savefig("graph.png", format="PNG")
        if show:
            plt.show()

    def __str__(self):
        table = Texttable()
        table.set_cols_align(["c", "c"])
        rows = [['Edge', 'Weight']]
        for edge in self._edges:
            rows.append([f"{edge.scr_vertex} -> {edge.dest_vertex}", f"{edge.weight}"])
        table.add_rows(rows)
        return str(table.draw())
