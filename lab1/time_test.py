from timeit import timeit

from source import adjacency_graph, edges_graph, records_graph


def timer(repeats=1):
    def decorator(f):
        def new_function():
            full_time = timeit(f, number=repeats)
            return round(full_time, 3)

        return new_function

    return decorator


class EGraph:
    @staticmethod
    @timer(repeats=10 ** 6)
    def vertex_neighbors():
        edges_graph.vertex_neighbors('P3')

    @staticmethod
    @timer(repeats=10 ** 6)
    def edges_number():
        edges_graph.edges_number()

    @staticmethod
    @timer(repeats=10 ** 6)
    def is_chain():
        edges_graph.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2'])

    @staticmethod
    @timer(repeats=10 ** 6)
    def vertex_by_weights_sum():
        edges_graph.vertex_by_weights_sum(weight=36)


class RGraph:
    @staticmethod
    @timer(repeats=10 ** 6)
    def vertex_neighbors():
        records_graph.vertex_neighbors('P3')

    @staticmethod
    @timer(repeats=10 ** 6)
    def edges_number():
        records_graph.edges_number()

    @staticmethod
    @timer(repeats=10 ** 6)
    def is_chain():
        records_graph.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2'])

    @staticmethod
    @timer(repeats=10 ** 6)
    def vertex_by_weights_sum():
        records_graph.vertex_by_weights_sum(weight=36)


class AGraph:
    @staticmethod
    @timer(repeats=10 ** 6)
    def vertex_neighbors():
        adjacency_graph.vertex_neighbors('P3')

    @staticmethod
    @timer(repeats=10 ** 6)
    def edges_number():
        adjacency_graph.edges_number()

    @staticmethod
    @timer(repeats=10 ** 6)
    def is_chain():
        adjacency_graph.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2'])

    @staticmethod
    @timer(repeats=10 ** 6)
    def vertex_by_weights_sum():
        adjacency_graph.vertex_by_weights_sum(weight=36)
