import pytest

from library import AdjacencyMatrix, AdjacencyMatrixGraph, EdgesListGraph, RecordsArrayGraph

@pytest.fixture(scope='class')
def a_matrix_fix():
    return AdjacencyMatrix([
            [0,2,0,0,0,0,0,0],
            [0,0,4,4,34,0,0,0],
            [5,0,0,0,5,0,0,0],
            [9,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,6,6],
            [0,2,0,8,0,0,0,0],
            [0,0,0,0,0,7,0,0],
            [0,0,0,0,0,0,0,0]
        ],
        ['N2', 'P3', 'E2', 'A3', 'P1', 'A2', 'N1', 'A1']
    )

@pytest.fixture(scope='class')
def adjancency_graph_fix(a_matrix_fix):
    return AdjacencyMatrixGraph(a_matrix_fix)

@pytest.fixture(scope='class')
def records_graph_fix(a_matrix_fix):
    return RecordsArrayGraph(a_matrix_fix)

@pytest.fixture(scope='class')
def edge_graph_fix(a_matrix_fix):
    return EdgesListGraph(a_matrix_fix)