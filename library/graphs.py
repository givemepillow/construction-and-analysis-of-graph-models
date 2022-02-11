from abc import ABC, abstractmethod

from library.types import Edge, Record
from library.adjacency_matrix import AdjacencyMatrix

import networkx as nx
import matplotlib.pyplot as plt
from texttable import Texttable


class Graph(ABC):
    @abstractmethod
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        self.adjacency_matrix = adjacency_matrix.get_adjanceny_matrix()
        self.vertexes = {}
        for i, v in enumerate(self.adjacency_matrix):
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
    def render(self):
        pass

class EdgesListGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        matrix = self.adjacency_matrix
        self.edges = [
            Edge(out_vertex=v1,in_vertex=v2, weight=matrix[v1][v2]) 
            for v1 in matrix for v2 in matrix[v1] if matrix[v1][v2] > 0
        ]

    def vertex_neighbors(self, vertex_name) -> list[str]:
        result = []
        for edge in self.edges:
            if vertex_name in (edge.in_vertex, edge.out_vertex):
                result.append(edge.in_vertex if edge.in_vertex != vertex_name else edge.out_vertex)
        return result

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        for i, vertex in enumerate(vertexes_sequence[:-1]):
            flag = True
            for egde in self.edges:
                if egde.out_vertex == vertex and egde.in_vertex == vertexes_sequence[i + 1]:
                    flag = False
                    break
            if flag: return False
        return True


    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        sum_w = {}
        for v in self.vertexes:
            for edge in self.edges:
                if v in (edge.in_vertex, edge.out_vertex):
                    sum_w[v] = edge.weight + sum_w[v] if v in sum_w else edge.weight
        return [k for k in sum_w if sum_w[k] > weight]

    def edges_number(self) -> list[str]:
        return len(self.edges)

    def render(self, save=False):
        graph = nx.DiGraph()
        graph.add_nodes_from([v for v in self.vertexes])
        graph.add_weighted_edges_from(((e.out_vertex, e.in_vertex, e.weight) for e in self.edges))
        plt.figure(figsize=(12,12))
        nx.draw(graph,
            pos=nx.spring_layout(graph, k=2),
            node_color='lightgreen',
            node_size=1000,
            with_labels=True
        )
        plt.savefig("graph.png", format="PNG")
    
    def __str__(self):
        table = Texttable()
        table.set_cols_align(["c", "c"])
        rows = [['Edge', 'Weight']]
        for edge in self.edges:
            rows.append([f"{edge.out_vertex} -> {edge.in_vertex}", f"{edge.weight}"])
        table.add_rows(rows)
        return str(table.draw())


class AdjacencyMatrixGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.__str__adjacency_matrix = adjacency_matrix.__str__

    def vertex_neighbors(self, vertex_name) -> list[str]:
        m = self.adjacency_matrix
        return [v for v in m if m[v][vertex_name] > 0 or m[vertex_name][v] > 0]

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        for i, vertex in enumerate(vertexes_sequence[:-1]):
            if self.adjacency_matrix[vertexes_sequence[i + 1]][vertex] != 0:
                return False
        return True

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        sum_w = {}
        for v in self.vertexes:
            for other in self.vertexes:
                if v not in sum_w:
                    sum_w[v] = 0
                sum_w[v] += self.adjacency_matrix[v][other]
                sum_w[v] += self.adjacency_matrix[other][v]
        return [k for k in sum_w if sum_w[k] > weight]

        

    def edges_number(self) -> list[str]:
        number = 0
        for v1 in self.vertexes:
            for v2 in self.vertexes:
                if self.adjacency_matrix[v2][v1] > 0:
                    number += 1
        return number

    def render(self):
        pass

    def __str__(self):
        return self.__str__adjacency_matrix()



class RecordsArrayGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.records = {}
        matrix = self.adjacency_matrix
        for vertex in self.vertexes:
            out_edges_weight, in_edges_weight = [], []
            parents, children = [], []
            for child in matrix[vertex].items():
                if child[1] > 0:
                    out_edges_weight.append(child[1])
                    children.append(child[0])
            for parent in matrix[vertex]:
                if matrix[parent][vertex] > 0:
                    in_edges_weight.append(matrix[parent][vertex])
                    parents.append(parent)

            self.records[vertex] = Record(
                vertex=vertex,
                vertex_number=self.vertexes[vertex],
                parents=parents,
                children=children,
                out_edges_weight=out_edges_weight,
                in_edges_weight=in_edges_weight
            )

    def vertex_neighbors(self, vertex_name) -> list[str]:
        return self.records[vertex_name].neighbors

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        for i, vertex in enumerate(vertexes_sequence[:-1]):
            if vertexes_sequence[i + 1] not in self.records[vertex].children:
                return False
        return True

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        return [r.vertex for r in self.records.values() if sum(r.incident_edges_weight) > weight]

    def edges_number(self) -> list[str]:
        edges = 0
        _vertexes = []
        for v1 in self.vertexes:
            for r in self.records.values():
                if r.vertex not in _vertexes and v1 in r.neighbors:
                    edges += 1
                    _vertexes.append(v1)
        return edges


    def render(self):
        pass

    def __str__(self) -> str:
        table = Texttable()
        table.set_cols_align(["c", "c", "r", "l"])
        rows = [['№', 'Vertex', 'Parents', 'Children']]
        for record in self.records.values():
            rows.append([record.vertex_number, record.vertex, record.parents, record.children])
        table.add_rows(rows)
        return str(table.draw())
