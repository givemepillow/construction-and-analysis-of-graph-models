from dataclasses import dataclass, field

__all__ = ['Edge', 'Record']

@dataclass
class Edge:
    out_vertex: str
    in_vertex: str
    weight: float

    def __str__(self):
        return f"{self.out_vertex} -> {self.in_vertex}: {self.weight}"

@dataclass
class Record:
    vertex: str
    vertex_number: int
    children_number: int = field(init=False, default=None)
    parents_number: int = field(init=False, default=None)
    neighbors_number: int = field(init=False, default=None)
    children: list[str]
    parents: list[str]
    neighbors: list[str] = field(init=False, default_factory=list)
    incident_edges_weight: list[Edge] = field(init=False, default_factory=list)
    in_edges_weight: list[Edge]
    out_edges_weight: list[Edge]

    def __post_init__(self):
        self.incident_edges_weight = self.in_edges_weight + self.out_edges_weight
        self.neighbors = self.children + self.parents
        self.children_number = len(self.children)
        self.parents_number = len(self.parents)
        self.neighbors_number = len(self.children) + len(self.parents)



