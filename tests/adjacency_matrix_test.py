import pytest

from library import AdjacencyMatrix


class TestAdjacencyMatrix:

    @pytest.mark.parametrize(
        'matrix, exception, names', [
            pytest.param([[1, 2, 3]], ValueError, [], id="Non square matrix"),
            pytest.param([[1]], ValueError, ['A', 'B'], id='Non correct names size'),
            pytest.param([[1, 2], [1, 'A']], TypeError, [], id='Non int matrix values'),
        ]
    )
    def test_raises(self, matrix, exception, names):
        with pytest.raises(exception):
            AdjacencyMatrix(names=names, matrix=matrix)
