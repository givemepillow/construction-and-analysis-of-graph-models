import pytest

from library import AdjacencyMatrixGraph, EdgesListGraph, RecordsArrayGraph


class TestAdjacencyMatrixGraph:
    def test_vertex_neighbors_1(self, adjancency_graph_fix):
        assert adjancency_graph_fix.vertex_neighbors('A1') == ['P1']

    def test_vertex_neighbors_2(self, adjancency_graph_fix):
        assert set(adjancency_graph_fix.vertex_neighbors('P3')) == set(['P1', 'N2', 'E2', 'A3', 'A2'])

    def test_is_chain_true(self, adjancency_graph_fix):
        assert adjancency_graph_fix.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2']) == True

    def test_is_chain_false(self, adjancency_graph_fix):
        assert adjancency_graph_fix.is_chain(['E2', 'N2', 'P3', 'A2', 'N1', 'A2']) == False

    def test_vertex_by_weights_sum(self, adjancency_graph_fix):
        assert adjancency_graph_fix.vertex_by_weights_sum(50) == ['P1']

    def test_vertex_by_weights_sum_all(self, adjancency_graph_fix):
        assert adjancency_graph_fix.vertex_by_weights_sum(0) == ['N2', 'P3', 'E2', 'A3', 'P1', 'A2', 'N1', 'A1']

    def test_edges_number(self, adjancency_graph_fix):
        assert adjancency_graph_fix.edges_number() == 12




class TestEdgesListGraph:
    def test_vertex_neighbors_1(self, edge_graph_fix):
        assert edge_graph_fix.vertex_neighbors('A1') == ['P1']

    def test_vertex_neighbors_2(self, edge_graph_fix):
        assert set(edge_graph_fix.vertex_neighbors('P3')) == set(['P1', 'N2', 'E2', 'A3', 'A2'])

    def test_is_chain_true(self, edge_graph_fix):
        assert edge_graph_fix.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2']) == True

    def test_is_chain_false(self, edge_graph_fix):
        assert edge_graph_fix.is_chain(['E2', 'N2', 'P3', 'A2', 'N1', 'A2']) == False

    def test_vertex_by_weights_sum(self, edge_graph_fix):
        assert edge_graph_fix.vertex_by_weights_sum(50) == ['P1']

    def test_vertex_by_weights_sum_all(self, edge_graph_fix):
        assert edge_graph_fix.vertex_by_weights_sum(0) == ['N2', 'P3', 'E2', 'A3', 'P1', 'A2', 'N1', 'A1']

    def test_edges_number(self, edge_graph_fix):
        assert edge_graph_fix.edges_number() == 12


class TestRecordsArrayGraph:
    def test_vertex_neighbors_1(self, records_graph_fix):
        assert records_graph_fix.vertex_neighbors('A1') == ['P1']

    def test_vertex_neighbors_2(self, records_graph_fix):
        assert set(records_graph_fix.vertex_neighbors('P3')) == set(['P1', 'N2', 'E2', 'A3', 'A2'])

    def test_is_chain_true(self, records_graph_fix):
        assert records_graph_fix.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2']) == True

    def test_is_chain_false(self, records_graph_fix):
        assert records_graph_fix.is_chain(['E2', 'N2', 'P3', 'A2', 'N1', 'A2']) == False

    def test_vertex_by_weights_sum(self, records_graph_fix):
        assert records_graph_fix.vertex_by_weights_sum(50) == ['P1']

    def test_vertex_by_weights_sum_all(self, records_graph_fix):
        assert records_graph_fix.vertex_by_weights_sum(0) == ['N2', 'P3', 'E2', 'A3', 'P1', 'A2', 'N1', 'A1']

    def test_edges_number(self, records_graph_fix):
        assert records_graph_fix.edges_number() == 12
