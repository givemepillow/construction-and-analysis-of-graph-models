from copy import deepcopy


class AdjacencyMatrix:
    _matrix: {}

    def __init__(self, matrix: list[list] | dict[dict], names: list[str] | None = None):
        """
        Получает список списков и список вершин и создаёт из них словарь словарей.
        :param matrix: список списков - матрица смежности пользователя.
        :param names: имена вершин.
        """
        if isinstance(matrix, dict):
            self._matrix = matrix
        else:
            names = names if names else list(map(str, range(0, len(matrix))))
            ad_matrix = dict()
            for key1, row in zip(names, matrix):
                ad_matrix[key1] = dict()
                for key2, value in zip(names, row):
                    ad_matrix[key1][key2] = value
            self._matrix = ad_matrix

    def get_adjacency_matrix(self):
        return deepcopy(self._matrix)

    def branch_length_estimation(self, v1, v2, new_vertex_name):
        new_matrix = self.get_adjacency_matrix()

        # Удаление указанные вершин из матрицы.
        del new_matrix[v1]
        del new_matrix[v2]
        for row in new_matrix.values():
            row.pop(v1)
            row.pop(v2)

        # Установка новой вершины.
        new_vertex = new_vertex_name
        new_matrix.update({new_vertex: {}})

        # Обновление расстояний между вершинами в новой матрице.
        print("РАСЧЁТЫ:")
        for vertex in new_matrix:
            if vertex not in (v1, v2, new_vertex):

                new_distance = (self._matrix[v1][vertex] + self._matrix[v2][vertex]) / 2
                new_matrix[new_vertex][vertex] = new_distance
                new_matrix[vertex][new_vertex] = new_distance
                print(f"{vertex}-{new_vertex} = "
                      f"({v1}-{vertex} + {v2}-{vertex}) / 2 = "
                      f"({self._matrix[v1][vertex]} + {self._matrix[v2][vertex]}) / 2 = {new_distance}")
            elif vertex == new_vertex:
                new_matrix[vertex][new_vertex] = 0
        self._matrix = new_matrix

    def smallest_distance(self) -> (float, (str, str)):
        _dist = min([v for r in self._matrix.values() for v in r.values() if v != 0])
        for row in self._matrix:
            for column in self._matrix[row]:
                if _dist == self._matrix[row][column]:
                    return _dist, (row, column)

    @property
    def size(self):
        return len(self._matrix)

    @staticmethod
    def square_grid(size):
        matrix = [[0 for _ in range(size ** 2)] for _ in range(size ** 2)]
        for v in range(size ** 2):
            r = v // size
            c = v % size
            if c < size:
                matrix[v][v + 1] = matrix[v + 1][v] = 1
            if r < size:
                matrix[v][v + size] = matrix[v + size][v] = 1
                if (r % 2 == 0 and c % 2 == 0) or (r % 2 == 0 and c % 2 == 0):
                    if c > 0:
                        matrix[v][v + size - 1] = matrix[v + size - 1][v] = 1
                    if c < size:
                        matrix[v][v + size + 1] = matrix[v]

        return AdjacencyMatrix(matrix)

    def __str__(self):
        max_label_len = max([len(str(key)) for key in self._matrix])
        max_label_len = 3 if max_label_len < 3 else max_label_len
        result = "[M] " + " " * (max_label_len - 3)
        for name in self._matrix:
            result += f"{name}".center(max_label_len, ' ') + ' '
        result += "\n " + " " * max_label_len
        for _ in self._matrix:
            result += f"-" * max_label_len + '-'
        result += "\n"
        for key in self._matrix:
            result += f"{key}".rjust(max_label_len, ' ') + '|'
            for value in self._matrix[key]:
                result += f"{self._matrix[key][value]}".center(max_label_len, ' ') + ' '
            result += "\n"
        return result
