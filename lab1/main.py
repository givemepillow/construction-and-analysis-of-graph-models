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

graph_edges = EdgesListGraph(ad_matrix)  # список рёбер
graph_records = RecordsArrayGraph(ad_matrix)  # список записей
graph_adjacency = AdjacencyMatrixGraph(ad_matrix)  # матрица смежности

print(graph_adjacency.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2']))
print(graph_records.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2']))
print(graph_edges.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2']))
# True
#
print(graph_adjacency)
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

print(graph_edges)
# +----------+--------+
# |   Edge   | Weight |
# +==========+========+
# | N2 -> P3 |   2    |
# +----------+--------+
# | P3 -> E2 |   4    |
# +----------+--------+
# | P3 -> A3 |   4    |
# +----------+--------+
# | P3 -> P1 |   34   |
# +----------+--------+
# | E2 -> N2 |   5    |
# +----------+--------+
# | E2 -> P1 |   5    |
# +----------+--------+
# | A3 -> N2 |   9    |
# +----------+--------+
# | P1 -> N1 |   6    |
# +----------+--------+
# | P1 -> A1 |   6    |
# +----------+--------+
# | A2 -> P3 |   2    |
# +----------+--------+
# | A2 -> A3 |   8    |
# +----------+--------+
# | N1 -> A2 |   7    |
# +----------+--------+


print(graph_records)
# +---+--------+--------------+--------------------+
# | № | Vertex |   Parents    |      Children      |
# +===+========+==============+====================+
# | 1 |   N2   | ['E2', 'A3'] | ['P3']             |
# +---+--------+--------------+--------------------+
# | 2 |   P3   | ['N2', 'A2'] | ['E2', 'A3', 'P1'] |
# +---+--------+--------------+--------------------+
# | 3 |   E2   |       ['P3'] | ['N2', 'P1']       |
# +---+--------+--------------+--------------------+
# | 4 |   A3   | ['P3', 'A2'] | ['N2']             |
# +---+--------+--------------+--------------------+
# | 5 |   P1   | ['P3', 'E2'] | ['N1', 'A1']       |
# +---+--------+--------------+--------------------+
# | 6 |   A2   |       ['N1'] | ['P3', 'A3']       |
# +---+--------+--------------+--------------------+
# | 7 |   N1   |       ['P1'] | ['A2']             |
# +---+--------+--------------+--------------------+
# | 8 |   A1   |       ['P1'] | []                 |
# +---+--------+--------------+--------------------+

graph_adjacency.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2'])
# True
graph_edges.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2'])
# True
graph_records.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2'])
# True

graph_adjacency.edges_number()
# 12
graph_edges.edges_number()
# 12
graph_records.edges_number()
# 12

graph_adjacency.vertex_neighbors('P3')
# ['P1', 'N2', 'E2', 'A3', 'A2']
graph_edges.vertex_neighbors('P3')
# ['P1', 'N2', 'E2', 'A3', 'A2']
graph_records.vertex_neighbors('P3')
# ['P1', 'N2', 'E2', 'A3', 'A2']

graph_adjacency.vertex_by_weights_sum(weight=36)
# ['P3', 'P1']
graph_edges.vertex_by_weights_sum(weight=36)
# ['P3', 'P1']
graph_records.vertex_by_weights_sum(weight=36)
# ['P3', 'P1']

graph_edges.render()
# PICTURE
