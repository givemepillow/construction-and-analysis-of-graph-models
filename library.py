# %%
class AdjacencyMatrix:
    __source_matrix: list[list]
    __adjanceny_matrix: dict[dict]

    def __init__(self, matrix: list[list], names: list = []):
        if len(matrix) != sum([len(matrix[i]) for i in range(len(matrix))])/len(matrix):
            raise ValueError("Матрица должна быть квадратной!")
        elif len(names) > 0 and (len(matrix) != len(set(names))):
             raise ValueError("Не соответстие вершин!")
        names = names if names else range(1, len(matrix) + 1)
        ad_matrix = {}
        for key1, row in zip(names, matrix):
            ad_matrix[key1] = dict()
            for key2, value in zip(names, row):
                ad_matrix[key1][key2] = value
        self.__adjanceny_matrix, self.__source_matrix = ad_matrix, matrix

    def __str__(self):
        result = "[M] "
        for name in self.__adjanceny_matrix.keys():
            result += f"{name}".rjust(3, ' ')
        result += "\n     "
        for name in self.__adjanceny_matrix:
            result += f"---"
        result += "\n"
        for key in self.__adjanceny_matrix:
            result += f"{key}".rjust(3, ' ') + '|'
            for value in self.__adjanceny_matrix[key].values():
                result += f"{value}".rjust(3, ' ')
            result += "\n"
        return result


# %%



