from copy import deepcopy


class AdjacencyMatrix:
    __adjacency_matrix: {}

    def __init__(self, matrix: list[list] | dict[dict], names: list[str] | None = None):
        """
        Получает список списков и список вершин и создаёт из них словарь словарей.
        :param matrix: список списков - матрица смежности пользователя.
        :param names: имена вершин.
        """
        if isinstance(matrix, dict):
            self.__adjacency_matrix = matrix
        else:
            self.__init_check(matrix, names)
            names = names if names else list(map(str, range(0, len(matrix))))
            ad_matrix = dict()
            for key1, row in zip(names, matrix):
                ad_matrix[key1] = dict()
                for key2, value in zip(names, row):
                    ad_matrix[key1][key2] = value
            self.__adjacency_matrix = ad_matrix

    def get_adjacency_matrix(self):
        return deepcopy(self.__adjacency_matrix)

    @staticmethod
    def square_grid(size):
        def repl():
            while True:
                yield lambda n: n % 2 == 0
                yield lambda n: n % 2 == 1

        matrix = [[0 for _ in range(size ** 2)] for _ in range(size ** 2)]
        for v in range(size ** 2):
            r = v // size
            c = v % size
            if c < size:
                matrix[v][v + 1] =  matrix[v + 1][v] = 1
            if r < size:
                matrix[v][v + size] = matrix[v + size][v] = 1
                if (r % 2 == 0 and c % 2 == 0) or (r % 2 == 0 and c % 2 == 0):
                    if c > 0:
                        matrix[v][v+size-1] = matrix[v+size-1][v] = 1
                    if c < size:
                        matrix[v][v + size +1] = matrix[v]


        return AdjacencyMatrix(matrix)

    @staticmethod
    def __init_check(matrix, names):
        if not isinstance(matrix, list) and all(map(lambda l: isinstance(l, list), matrix)):
            raise TypeError("Матрица задаётся списком списков!")
        elif not all([isinstance(x, int) for row in matrix for x in row]):
            raise TypeError("Значения матрицы должны быть целыми числами!")
        elif len(matrix) != sum([len(matrix[i]) for i in range(len(matrix))]) / len(matrix):
            raise ValueError("Матрица должна быть квадратной!")
        elif names and len(names) > 0 and (len(matrix) != len(set(names))):
            raise ValueError("Не соответстие вершин!")

    def __str__(self):
        max_label_len = max([len(str(key)) for key in self.__adjacency_matrix])
        max_label_len = 3 if max_label_len < 3 else max_label_len
        result = "[M] " + " " * (max_label_len - 3)
        for name in self.__adjacency_matrix.keys():
            result += f"{name}".center(max_label_len, ' ') + ' '
        result += "\n " + " " * max_label_len
        for _ in self.__adjacency_matrix:
            result += f"-" * max_label_len + '-'
        result += "\n"
        for key in self.__adjacency_matrix:
            result += f"{key}".rjust(max_label_len, ' ') + '|'
            for value in self.__adjacency_matrix[key].values():
                result += f"{value}".center(max_label_len, ' ') + ' '
            result += "\n"
        return result
