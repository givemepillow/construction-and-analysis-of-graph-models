from collections.abc import Iterable
from math import ceil
from random import randint, choice

import numpy as np
from cycler import cycler
from matplotlib import pyplot as plt

from library import EdgesListGraphOnEdges, EdgesListGraph, AdjacencyMatrix, Graph
from library.types import Edge


def make_grid(p: float | list | tuple, size: int):
    _grid = {j: {i: 0 for i in range(size)} for j in range(size)}
    if isinstance(p, Iterable):
        p_list = list(p)
    elif not isinstance(p, list | tuple):
        p_list = [p]
    else:
        p_list = p
    for _p in p_list:
        number = ceil(((size ** 2) * _p) / 4)
        for _ in range(number):
            r, c = randint(0, size - 2), randint(0, size - 2)
            _grid[r][c] = 1
            _grid[r][c + 1] = 1
            _grid[r + 1][c] = 1
            _grid[r + 1][c + 1] = 1
    return _grid


def make_adjacency_matrix(_grid):
    grid_size = len(_grid)
    i = -1
    _vertexes = []
    for row in _grid.values():
        for cell in row.values():
            i += 1
            if cell != 0:
                _vertexes.append(i)
    _matrix = {v: {v: 0 for v in _vertexes} for v in _vertexes}
    for r_index, row in _grid.items():
        for c_index, col in row.items():
            if col:
                current_vertex = (r_index * grid_size) + c_index
                if c_index < (grid_size - 1) and _grid[r_index][c_index + 1] == 1:
                    _matrix[current_vertex][(r_index * grid_size) + (c_index + 1)] = 1
                if r_index < (grid_size - 1) and _grid[r_index + 1][c_index] == 1:
                    _matrix[current_vertex][((r_index + 1) * grid_size) + c_index] = 1
    return _matrix


# def make_edges(_grid):
#     size = len(_grid)
#     _edges = []
#     for r_index, row in _grid.items():
#         for c_index, col in row.items():
#             if col:
#                 current_vertex = (r_index * size) + c_index
#                 # _edges.append(Edge(scr_vertex=current_vertex, dest_vertex=current_vertex, weight=0))
#                 if c_index < size - 1 and _grid[r_index][c_index + 1] == 1:
#                     _edges.append(Edge(
#                         scr_vertex=current_vertex,
#                         dest_vertex=(r_index * size) + (c_index + 1),  # right neighbor
#                         weight=1
#                     ))
#                 if r_index < size - 1 and _grid[r_index + 1][c_index] == 1:
#                     _edges.append(Edge(
#                         scr_vertex=current_vertex,
#                         dest_vertex=((r_index + 1) * size) + c_index,  # bottom neighbor
#                         weight=1
#                     ))
#     return _edges


def draw_grid(grid: dict[dict]):
    n_rows = len(grid)
    n_cols = len(grid)

    cell_id = []
    cell_value = []

    for r_index, row in grid.items():
        for c_index, col in row.items():
            cell_id.append(r_index * len(grid) + c_index)
            cell_value.append(col)

    data = np.zeros(n_rows * n_cols)
    data[cell_id] = cell_value
    data = np.ma.array(data.reshape((n_rows, n_cols)), mask=data == 0)

    fig, ax = plt.subplots()
    ax.imshow(data, cmap="Spectral", origin="lower", vmin=0)

    ax.set_xticks(np.arange(n_cols + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(n_rows + 1) - 0.5, minor=True)
    ax.grid(which="minor")
    ax.tick_params(which="minor", size=0)
    plt.gca().invert_yaxis()
    plt.show()


def graph_degrees_spectrum(graph: Graph):
    sp = {v: len(graph.vertex_neighbors(v)) for v in graph.vertexes}
    degrees = set(sp.values())
    colors = zip(degrees, cycler('color', ['MediumPurple', 'PaleVioletRed', 'YellowGreen', 'Tomato']))
    bar_color = {d: p for d, p in colors}
    data = {}
    for vertex, deg in sp.items():
        count = data.setdefault(deg, 0) + 1
        data[deg] = count
    for d in data.values():
        plt.axhline(y=d, color='Silver', linestyle='--')
    for deg, count in data.items():
        plt.bar(str(deg), count, color=bar_color[deg]['color'])

    plt.xlabel('Степень вершины')
    plt.ylabel('Количество вершин')
    plt.title(f'Спектр степеней вершин')
    plt.show()


def column_vertexes(grid) -> (list, list):
    _size = len(grid)
    i = -1
    _column_1, _column_2 = [], []
    for row in grid.values():
        for cell in row.values():
            i += 1
            if cell != 0:
                if i % _size == 0:
                    _column_1.append(i)
                elif i % _size == _size - 1:
                    _column_2.append(i)
    return _column_1, _column_2


def path_existence(column_1, column_2, graph: Graph):
    for c1 in column_1:
        for c2 in column_2:
            if graph.bfs(c1, c2):
                return True
    return False


P = choice(np.arange(0.05, 1.05, 0.05))
print(f"{P=}")
main_grid = make_grid(P, 10)
adjacency_matrix = make_adjacency_matrix(main_grid)
g = EdgesListGraph(AdjacencyMatrix(adjacency_matrix, names=list(adjacency_matrix.keys())))
# print(g)
# print(g.edges_number())
# print(g.vertexes_number())
draw_grid(main_grid)
graph_degrees_spectrum(g)
g.render(
    planar=False,
    edge_labels=False,
    font_size=6,
    node_size=75,
    arrow_size=4,
    grid=main_grid
)
exit()
#
# data = {}
# for p in np.arange(0.05, 1.05, 0.05):
#     yes = 0
#     for _ in range(1000):
#         _grid = make_grid(p, 10)
#         c1, c2 = column_vertexes(_grid)
#         adjacency_matrix = make_adjacency_matrix(_grid)
#         g = EdgesListGraph(AdjacencyMatrix(adjacency_matrix, names=list(adjacency_matrix.keys())))
#         if path_existence(c1, c2, g):
#             yes += 1
#         data[round(p, 3)] = yes / 1000
#     # print(path_existence(c1, c2, g))
#
# y = data.values()
# x = data.keys()
#
# fig, ax = plt.subplots()
# plt.figure(figsize=(10, 15), dpi=200)
# ax.plot(x, y, color='DarkOrchid', lw=3)
# ax.fill_between(x, 0, y, alpha=.3, color='DarkOrchid')
# ax.set_title('График вероятности существования пути\n\
# между первым и последним столбцами решетки')
# ax.set_ylabel('Вероятность существования пути')
# ax.set_xlabel('Вероятность закрашивания клетки ($\\rho$)')
# ax.grid(True, linestyle="--", color='MediumPurple', alpha=.3)
# # for _x, _y in zip(x[15:-1:2], y[15:-1:2]):
# #     plt.annotate(
# #         (_x, _y),
# #         textcoords="offset points",
# #         xytext=(0, 10),
# #         ha='center'
# #     )
# plt.show()
