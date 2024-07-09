import pickle
import networkx as nx
import random


def generate(numberNodes):
    graph = nx.empty_graph(numberNodes)
    return graph


def add_edges(graph, avg_edges):
    graphSize = graph.number_of_nodes()
    length = (avg_edges * graphSize) / 2

    while length > 0:
        first_node = random.randint(0, graphSize)
        second_node = random.randint(0, graphSize)

        if first_node != second_node and graph.has_edge(first_node, second_node) == False:
            graph.add_edge(first_node, second_node)
            length -= 1

    return graph


def save144(graph, current, half):
    if half:
        pathStart = 'graphs144 and a half/graph144_'
        pathEnd = '.pickle'
        fileName = pathStart + str(current) + pathEnd
        pickle.dump(graph, open(fileName, 'wb'))
    else:
        pathStart = 'graphs144/graph144_'
        pathEnd = '.pickle'
        fileName = pathStart + str(current) + pathEnd
        pickle.dump(graph, open(fileName, 'wb'))


def save81(graph, current, half):
    if half:
        pathStart = 'graphs81 and a half/graph81_'
        pathEnd = '.pickle'
        fileName = pathStart + str(current) + pathEnd
        pickle.dump(graph, open(fileName, 'wb'))
    else:
        pathStart = 'graphs81/graph81_'
        pathEnd = '.pickle'
        fileName = pathStart + str(current) + pathEnd
        pickle.dump(graph, open(fileName, 'wb'))


def make_graphs(numberToMake):
    current = 1

    for i in range(1, 15):
        half = False
        for j in range(0, numberToMake):
            graph144 = generate(144)
            graph81 = generate(81)

            graph144 = add_edges(graph144, i)
            graph81 = add_edges(graph81, i)

            save144(graph144, current, half)
            save81(graph81, current, half)

            current += 1

        current -= 10
        half = True
        for j in range(0, numberToMake):
            if i == 14:
                break
            graph144 = generate(144)
            graph81 = generate(81)

            graph144 = add_edges(graph144, i + 0.5)
            graph81 = add_edges(graph81, i + 0.5)

            save144(graph144, current, half)
            save81(graph81, current, half)

            current += 1




if __name__ == '__main__':
    # Makes the final graphs to use:
    make_graphs(10)  # The variable passed through is the number of graphs per average connectivity


