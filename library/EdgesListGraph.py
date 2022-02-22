import networkx as nx
import matplotlib.pyplot as plt
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
        neighbors = []
        for edge in self.edges:
            if vertex in (edge.dest_vertex, edge.scr_vertex):
                neighbors.append(edge.dest_vertex if edge.dest_vertex != vertex else edge.scr_vertex)
        return neighbors

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        for src_vertex, dest_vertex in zip(vertexes_sequence[:-1], vertexes_sequence[1::]):
            flag = True
            for edge in self.edges:
                if edge.scr_vertex == src_vertex and edge.dest_vertex == dest_vertex:
                    flag = False
                    break
            if flag:
                return False
        return True if len(vertexes_sequence) == len(set(vertexes_sequence)) else False

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        weights_sum = {}
        for v in self.vertexes:
            for edge in self.edges:
                if v in (edge.dest_vertex, edge.scr_vertex):
                    weights_sum[v] = (edge.weight + weights_sum[v]) if v in weights_sum else edge.weight
        return [v for v in weights_sum if weights_sum[v] > weight]

    def edges_number(self) -> list[str]:
        return len(self.edges)

    def render(self, save=False, show=False):
        graph = nx.DiGraph()
        graph.add_nodes_from([v for v in self.vertexes])
        graph.add_weighted_edges_from(((e.scr_vertex, e.dest_vertex, e.weight) for e in self.edges))
        plt.figure(figsize=(12, 12))
        nx.draw(graph,
                pos=nx.spring_layout(graph, k=2),
                node_color='lightgreen',
                node_size=1000,
                with_labels=True
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
