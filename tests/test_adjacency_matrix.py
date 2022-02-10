import pytest

from library import AdjacencyMatrix


def test_non_square_matrix():
    with pytest.raises(ValueError):
        AdjacencyMatrix([[1,2,3]])

def test_non_equal_names():
    with pytest.raises(ValueError):
        AdjacencyMatrix([[1]], ['A', 'B'])

def test_non_corret_matrix_format():
    with pytest.raises(TypeError):
        AdjacencyMatrix(45)

def test_non_corret_names_format():
    with pytest.raises(TypeError):
        AdjacencyMatrix([[1,2],[1,2]], names=[(), 'as'])
