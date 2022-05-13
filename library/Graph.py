from abc import ABC, abstractmethod

from library.AdjacencyMatrix import AdjacencyMatrix


class Graph(ABC):
    def __init__(self, adjacency_matrix: AdjacencyMatrix):
        if adjacency_matrix:
            self.adj_matrix = adjacency_matrix.get_adjacency_matrix()
            self._vertexes = {}
            for i, v in enumerate(self.adj_matrix):
                self._vertexes[v] = i + 1
        else:
            self.adj_matrix = {}
            self._vertexes = {}

    def bfs(self, start_node, goal_node):
        visited = set()

        def _bfs(start, goal):
            visited.add(start)
            neighbors = set(self.vertex_neighbors(start)) - visited
            if goal_node in neighbors:
                return True
            else:
                for n in neighbors:
                    if _bfs(n, goal):
                        return True
                return False

        return _bfs(start_node, goal_node)

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
    def edges_number(self) -> int:
        pass

    @abstractmethod
    def render(self, save=False, show=False):
        pass

    @abstractmethod
    def size(self) -> bytes:
        pass

    @property
    def vertexes(self):
        return self._vertexes
