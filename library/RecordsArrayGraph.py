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
            for child in self.adj_matrix[vertex].items():
                if child[1] > 0:
                    out_edges_weight.append(child[1])
                    children.append(child[0])
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

    def vertex_neighbors(self, vertex_name) -> list[str]:
        return self.records[vertex_name].neighbors

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        for i, vertex in enumerate(vertexes_sequence[:-1]):
            if vertexes_sequence[i + 1] not in self.records[vertex].children:
                return False
        return True

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        return [r.vertex for r in self.records.values() if sum(r.incident_edges_weight) > weight]

    def edges_number(self) -> int:
        edges_number = 0
        marked = []
        for v in self.vertexes:
            for record in self.records.values():
                if record.vertex not in marked and v in record.neighbors:
                    edges_number += 1
                    marked.append(v)
        return edges_number

    def size(self) -> bytes:
        return asizeof(self.records)

    def render(self, save=False, show=False):
        pass

    def __str__(self) -> str:
        table = Texttable()
        table.set_cols_align(["c", "c", "r", "l"])
        rows = [['№', 'Vertex', 'Parents', 'Children']]
        for record in self.records.values():
            rows.append([record.vertex_number, record.vertex, record.parents, record.children])
        table.add_rows(rows)
        return str(table.draw())
