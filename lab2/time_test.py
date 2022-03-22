from timeit import timeit, Timer

from library import EdgesListGraph, AdjacencyMatrix


def timer(repeats=1):
    def decorator(f):
        def new_function(*args, **kwargs):
            full_time = Timer(lambda: f(*args, **kwargs))
            return round(full_time.timeit(repeats), 3)

        return new_function

    return decorator


def test():
    test_graphs = [EdgesListGraph(AdjacencyMatrix.square_grid(size=i)) for i in range(1, 26)]

    @timer(1000)
    def run(g):
        g.mst()

    import matplotlib.pyplot as plt

    y = [run(g) for g in test_graphs]
    x = [i for i in range(1, len(test_graphs) + 1)]

    fig, ax = plt.subplots()
    ax.plot(x, y, color='deepskyblue', lw=3)
    ax.fill_between(x, 0, y, alpha=.3)
    ax.set_title('График зависимости быстродействия алгоритма\nот количества узлов в графе')
    ax.set_ylabel('Время в миллисекундах')
    ax.set_xlabel('Количество узлов')
    for _x, _y in zip(x[15:-1:2], y[15:-1:2]):
        label = f"{_y} мс"
        plt.annotate(
            label,
            (_x, _y),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center'
        )
    plt.show()
    print(y)

