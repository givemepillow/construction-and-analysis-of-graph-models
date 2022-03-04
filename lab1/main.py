import time_test as tt
from source import adjacency_graph, records_graph, edges_graph


def cli(prompt1, prompt2):
    def run_graph(graph):
        print(prompt1)
        while True:
            match input("Ввод: "):
                case '0':
                    print(graph)
                case '1':
                    v = input("Введите вершину: ")
                    print(graph.vertex_neighbors(v))
                case '2':
                    seq = input("Введите последовательность вершин через пробел: ")
                    print('Да' if graph.is_chain(seq.split()) else 'Нет')
                case '3':
                    v = input("Введите вес: ")
                    print(graph.vertex_by_weights_sum(int(v)))
                case '4':
                    print("Кол-во рёбер: ", graph.edges_number())
                case 'exit':
                    return

    while True:
        print(prompt2)
        match input("Ввод: "):
            case '1':
                run_graph(adjacency_graph)
            case '2':
                run_graph(edges_graph)
            case '3':
                run_graph(records_graph)
            case '4':
                test_graphs = tuple(zip(
                    (tt.AGraph, tt.EGraph, tt.RGraph), ('Матрица смежности', 'Список рёбер', 'Список записей')
                ))
                print("Оценка времени выполнения.")
                print("\nПоиск соседей: ")
                for g, name in test_graphs:
                    t = g.vertex_neighbors()
                    print(f"{name.upper()}: 10^6 раз - {t} сек. Среднее время: {t} мкс.")
                print("\nСумма инцидентных рёбер: ")
                for g, name in test_graphs:
                    t = g.vertex_by_weights_sum()
                    print(f"{name.upper()}: 10^6 раз - {t} сек. Среднее время: {t} мкс.")
                print("\nКол-во рёбер: ")
                for g, name in test_graphs:
                    t = g.edges_number()
                    print(f"{name.upper()}: 10^6 раз - {t} сек. Среднее время: {t} мкс.")
                print("\nПроверка на цепь: ")
                for g, name in test_graphs:
                    t = g.is_chain()
                    print(f"{name.upper()}: 10^6 раз - {t} сек. Среднее время: {t} мкс.")
            case '5':
                graphs = zip(
                    (adjacency_graph, edges_graph, records_graph),
                    ('Матрица смежности', 'Список рёбер', 'Список записей')
                )
                for g, name in graphs:
                    print(f"{name.upper()}: {g.size()} байт.")
            case 'exit':
                return


cli(
    prompt1="\nВведите, что хотите сделать:\n"
            "0 - Отобразить граф.\n"
            "1 - Вывод всех соседей заданной вершины.\n"
            "2 - Ответ, образует ли заданная последовательность вершин цепь.\n"
            "3 - Вывести номера вершин, сумма весов инцидентных ребер которых больше заданной величины.\n"
            "4 - Получить количество рёбер в графе.\n"
            "(Для выхода введите - exit.)\n",

    prompt2="\nВыберете граф:\n"
            "1 - Граф, представленный матрицей смежности.\n"
            "2 - Граф, представленный списком рёбер.\n"
            "3 - Граф, представленный списком записей\n"
            "4 - Оценка времени выполнения.\n"
            "5 - Размеры содержащего объекта.\n"
            "(Для выхода введите - exit.)\n"
)

# print(tt.EGraph.is_chain())
# print(tt.EGraph.vertex_neighbors())
# print(tt.EGraph.vertex_by_weights_sum())
# print(tt.EGraph.edges_number())

# edges_graph.render(show=True)

# print(f"{adjacency_graph.vertex_neighbors('P3')=}")
# print(f"{adjacency_graph.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A2'])=}")
# print(f"{adjacency_graph.vertex_by_weights_sum(weight=36)=}")
# print(f"{adjacency_graph.edges_number()=}")

# print(f"{edges_graph.vertex_neighbors('P2')=}")
# print(f"{edges_graph.is_chain(['E2', 'N2', 'P3', 'P1', 'N1', 'A1'])=}")
# print(f"{edges_graph.vertex_by_weights_sum(weight=36)=}")
# print(f"{edges_graph.edges_number()=}")

# print(f"{edges_graph.vertex_neighbors('E2')=}")
# print(f"{edges_graph.is_chain(['E2', 'N2', 'P3', 'P1', 'N1'])=}")
# print(f"{edges_graph.vertex_by_weights_sum(weight=6)=}")
# print(f"{edges_graph.edges_number()=}")

# print(graph_adjacency.size())
# print(graph_records.size())
# print(graph_edges.size())
