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

    def vertex_neighbors(self, vertex_name) -> list[str]:
        return self.records[vertex_name].neighbors if vertex_name in self.records else []

    def is_chain(self, vertexes_sequence: list[str]) -> bool:
        for src_vertex, dest_vertex in zip(vertexes_sequence[:-1], vertexes_sequence[1::]):
            if dest_vertex not in self.records[src_vertex].children:
                return False
        return True

    def vertex_by_weights_sum(self, weight: float) -> list[str]:
        return [r.vertex for r in self.records.values() if sum(r.incident_edges_weight) > weight]

    def edges_number(self) -> int:
        return sum((len(r.children) for r in self.records.values()))

    def size(self) -> bytes:
        return asizeof(self.records)

    def render(self, save=False, show=False):
        pass

    def __str__(self) -> str:
        table = Texttable()
        table.set_cols_align(["c", "c", "r", "l", "r", "l"])
        rows = [['№', 'Vertex', 'Parents', 'Children', "Out weights", "In weights"]]
        for r in self.records.values():
            rows.append([
                r.vertex_number,
                r.vertex,
                r.parents,
                r.children,
                r.out_edges_weight,
                r.in_edges_weight
            ])
        return str(table.add_rows(rows).draw())
