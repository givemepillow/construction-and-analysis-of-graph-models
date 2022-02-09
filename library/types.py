from dataclasses import dataclass

__all__ = ['Edge', 'Vertex']

@dataclass
class Vertex:
    name: str

    def __str__(self):
        return self.name

@dataclass
class Edge:
    out_vertex: Vertex
    in_vertex: Vertex
    weight: float

    def __str__(self):
        return f"{self.out_vertex} -> {self.in_vertex}: {self.weight}"




