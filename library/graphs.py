from abc import ABC, abstractmethod

from library.types import Edge, Record
from library.adjacency_matrix import AdjacencyMatrix

import networkx as nx
import matplotlib.pyplot as plt

class Graph(ABC):
    @abstractmethod
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        self.adjacency_matrix = adjacency_matrix.get_adjanceny_matrix()
        self.vertexes = {}
        for i, v in enumerate(self.adjacency_matrix):
            self.vertexes[v] = i + 1

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
        return '\n'.join(map(str, self.edges))


class AdjacencyMatrixGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.__str__adjacency_matrix = adjacency_matrix.__str__   

    def render(self):
        pass

    def __str__(self):
        return self.__str__adjacency_matrix()



class RecordsArrayGraph(Graph):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        super().__init__(adjacency_matrix)
        self.records = []
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

            self.records.append(Record(
                vertex=vertex,
                vertex_number=self.vertexes[vertex],
                parents=parents,
                children=children,
                out_edges_weight=out_edges_weight,
                in_edges_weight=in_edges_weight
            ))

    def render(self):
        pass

    def __str__(self) -> str:
        result = ''
        for r in self.records:
            result += f"{r}\n"
        return result
