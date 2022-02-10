from collections import OrderedDict
from copy import deepcopy


class AdjacencyMatrix:
    __adjanceny_matrix: OrderedDict[OrderedDict]

    def __init__(self, matrix: list[list], names: list[str] = []):
        if not (isinstance(matrix, list) and isinstance(matrix[0], list)):
            raise TypeError("Матрица задаётся списоком списков!")
        elif not (isinstance(names, list) and (len(names) == 0 or isinstance(names[0], str))):
            raise TypeError("Имена задаются списком строк!")
        elif len(matrix) != sum([len(matrix[i]) for i in range(len(matrix))])/len(matrix):
            raise ValueError("Матрица должна быть квадратной!")
        elif len(names) > 0 and (len(matrix) != len(set(names))):
             raise ValueError("Не соответстие вершин!")
        names = names if names else range(1, len(matrix) + 1)
        ad_matrix = OrderedDict()
        for key1, row in zip(names, matrix):
            ad_matrix[key1] = OrderedDict()
            for key2, value in zip(names, row):
                ad_matrix[key1][key2] = value
        self.__adjanceny_matrix = ad_matrix

    def get_adjanceny_matrix(self):
        return deepcopy(self.__adjanceny_matrix)

    def __str__(self):
        max_label_len = max([len(str(key)) for key in self.__adjanceny_matrix])
        max_label_len = 3 if max_label_len < 3 else max_label_len
        result = "[M] " + " " * (max_label_len - 3)
        for name in self.__adjanceny_matrix.keys():
            result += f"{name}".center(max_label_len, ' ') + ' '
        result += "\n " + " " * max_label_len
        for name in self.__adjanceny_matrix:
            result += f"-" * max_label_len + '-'
        result += "\n"
        for key in self.__adjanceny_matrix:
            result += f"{key}".rjust(max_label_len, ' ') + '|'
            for value in self.__adjanceny_matrix[key].values():
                result += f"{value}".center(max_label_len, ' ') + ' '
            result += "\n"
        return result
