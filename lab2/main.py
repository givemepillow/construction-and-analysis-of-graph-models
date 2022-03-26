from library import AdjacencyMatrix, EdgesListGraph
from lab2.time_test import test

my_graph = AdjacencyMatrix(
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

g = EdgesListGraph(my_graph)
# # g.render(show=True, planar=False)
# # g.render(show=True)
for vertex in ['N2', 'P3', 'E2', 'A3', 'P1', 'A2', 'N1', 'A1']:

    mst = g.mst(vertex)
    g.render(show=True, planar=True, highlights=mst.edges)
    input(f"MST"
          f"-tree from {vertex} with weights sum {mst.weights_sum}")

#
# square_g = EdgesListGraph(AdjacencyMatrix.square_grid(size=4))
# square_g.render(show=True, planar=False, highlights=square_g.mst().edges)
# print(AdjacencyMatrix.square_grid(size=2))

# test()

