from cycler import cycler

from library import AdjacencyMatrix, EdgesListGraph
from library.types import Edge

#
# matrix = AdjacencyMatrix(
#     matrix=[
#         [0, 9, 3, 6, 8, 9, 9, 2, 3, 2],
#         [1, 0, 7, 4, 1, 4, 2, 4, 4, 1],
#         [1, 1, 0, 1, 5, 6, 1, 1, 1, 9],
#         [1, 1, 1, 0, 5, 1, 4, 1, 4, 9],
#         [1, 1, 1, 1, 0, 1, 4, 1, 4, 9],
#         [1, 1, 1, 1, 1, 0, 1, 1, 7, 1],
#         [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 0, 8, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
#     ],
#     names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# )


matrix = AdjacencyMatrix(
    matrix=[
        [0, 17, 21, 31, 23],
        [17, 0, 30, 34, 21],
        [21, 30, 0, 28, 39],
        [31, 34, 28, 0, 43],
        [23, 21, 39, 43, 0]
    ],
    names=['a', 'b', 'c', 'd', 'e']
)

# matrix = AdjacencyMatrix(
#     matrix=[
#         [0, 14, 24, 32, 24, 32, 16, 26, 28, 14],
#         [14, 0, 10, 24, 20, 30, 34, 22, 32, 24],
#         [24, 10, 0, 28, 16, 10, 30, 34, 12, 18],
#         [32, 24, 28, 0, 16, 20, 26, 22, 26, 22],
#         [24, 20, 16, 16, 0, 26, 18, 30, 24, 16],
#         [32, 30, 10, 20, 26, 0, 16, 12, 26, 20],
#         [16, 34, 30, 26, 18, 16, 0, 22, 28, 22],
#         [26, 22, 34, 22, 30, 12, 22, 0, 28, 26],
#         [28, 32, 12, 26, 24, 26, 28, 28, 0, 24],
#         [14, 24, 18, 22, 16, 20, 22, 26, 24, 0]
#     ],
#     names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# )

init_graph = EdgesListGraph(matrix)
init_graph.render(show=True, planar=False, node_size=100, node_color='#f1c0e8')


# Генератор имён вершин
def vertex_names():
    while True:
        postfix = 0
        for v in set('suvwrytopqz'):
            yield f"{v}{postfix if postfix else ''}"
        postfix += 1


graph = EdgesListGraph()
names = vertex_names()
distances = {}
print("Начальная матрица:\n")

# Цикл выполняющий кластеризацию до тех пор,
# пока матрица расстояний (смежности) > 1 x 1.
while matrix.size - 1:
    # Получаем наименьшее расстояние и вершины соответствующие ему.
    dist, (v1, v2) = matrix.smallest_distance()
    half = dist / 2
    print(matrix, end='')
    print(f"# Кратчайшее расстояние: {v1}-{v2}: {dist}\n")

    vertex = next(names) if matrix.size != 2 else "(X)"

    # Добавляем выбранные вершины в кластерное дерево.
    graph.add(Edge(v1, vertex, half if v1 not in distances else half - distances[v1]))
    graph.add(Edge(v2, vertex, half if v2 not in distances else half - distances[v2]))

    print(f"Новая вершина:  {vertex}")
    print(
        f"Добавленные рёбра: "
        f"{v1}-{vertex}: {half if v1 not in distances else half - distances[v1]} и "
        f"{v2}-{vertex}: {half if v2 not in distances else half - distances[v2]}"
    )
    # Вызов метода обновления матрицы смежности.
    matrix.branch_length_estimation(v1, v2, new_vertex_name=vertex)
    distances[vertex] = half

graph.render(show=True, planar=False, node_size=100, node_color='#f1c0e8')
