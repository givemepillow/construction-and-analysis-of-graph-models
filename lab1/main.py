import time_test as tt
from source import adjacency_graph, records_graph, edges_graph


def cli():
    graph = None
    test_graph = None
    prompt1 = "Выберете граф:\n" \
              "1 - Граф, представленный матрицей смежности.\n" \
              "2 - Граф, представленный списком рёбер.\n" \
              "3 - Граф, представленный списком записей\n"

    print(prompt1)

    answer = input("Введите число: ")

    match answer:
        case '1':
            graph, test_graph = adjacency_graph, tt.AGraph
        case '2':
            graph, test_graph = edges_graph, tt.EGraph
        case '3':
            graph, test_graph = records_graph, tt.RGraph

    prompt2 = "Введите, что хотите сделать:\n1 - Вывод всех соседей заданной вершины.\n" \
              "2 - Ответ, образует ли заданная последовательнсть вершин цепь.\n" \
              "3 - Вывести номера вершин, сумма весов инцидентных ребер которых больше заданной величины.\n" \
              "4 - Получить количество рёбер в графе.\n" \
              "5 - Вывести размер содержашего объекта.\n" \
              "6 - Оценить время выполнения каждого метода.\n" \
              "(Для выхода из программы нажмите ввод.)\n"

    print(prompt2)

    while True:
        answer = input("Введите число: ")
        match answer:
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
            case '5':
                print(f"Размер содержащего обекта {graph.size()} байт.")
            case '6':
                print("Оценка времени выполнения.\n")
                t = test_graph.vertex_neighbors()
                print(f"Поиск соседей: 10^6 раз - {t} сек. Среднее время: {t} мкс | {t * 1000} мс.")
                t = test_graph.vertex_by_weights_sum()
                print(f"Сумма инцидентных рёбер: 10^6 раз - {t} сек. Среднее время: {t} мкс | {t * 1000} мс.")
                t = test_graph.edges_number()
                print(f"Кол-во рёбер: 10^6 раз - {t} сек. Среднее время: {t} мкс | {t * 1000} мс.")
                t = test_graph.is_chain()
                print(f"Проверка на цепь: 10^6 раз - {t} сек. Среднее время: {t} мкс | {t * 1000} мкс.\n")
            case _:
                print("До свидания.")
                break


cli()

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
