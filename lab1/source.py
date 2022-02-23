from library import AdjacencyMatrix, RecordsArrayGraph, EdgesListGraph, AdjacencyMatrixGraph

# ВАРИАНТ 10

# [M]  N2  P3  E2  A3  P1  A2  N1  A1
#     --------------------------------
#  N2| 0   2   0   0   0   0   0   0
#  P3| 0   0   4   4   34  0   0   0
#  E2| 5   0   0   0   5   0   0   0
#  A3| 9   0   0   0   0   0   0   0
#  P1| 0   0   0   0   0   0   6   6
#  A2| 0   2   0   8   0   0   0   0
#  N1| 0   0   0   0   0   7   0   0
#  A1| 0   0   0   0   0   0   0   0

ad_matrix = AdjacencyMatrix(
    names=['N2', 'P3', 'E2', 'A3', 'P1', 'A2', 'N1', 'A1'],
    matrix=[
        [0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 4, 34, 0, 0, 0],
        [5, 0, 0, 0, 5, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 6],
        [0, 2, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
)

edges_graph = EdgesListGraph(ad_matrix)  # список рёбер
records_graph = RecordsArrayGraph(ad_matrix)  # список записей
adjacency_graph = AdjacencyMatrixGraph(ad_matrix)  # матрица смежности
