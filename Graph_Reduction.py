import networkx as nx


def reduction1(graph, k_colouring):  # Remove Underconstrained Nodes
    nodes = list(graph.nodes())
    for i in nodes:
        if len(list(graph.neighbors(i))) < k_colouring:
            graph.remove_node(i)

    return graph


def reduction2(graph):  # Remove Subsumed Nodes
    nodes = list(graph.nodes())
    for i in nodes:
        for j in range(i+1, len(nodes)):
            if i in graph.nodes() and j in graph.nodes():
                if graph.neighbors(j) in graph.neighbors(i) and i not in graph.neighbors(j):
                    graph.remove_node(j)

    return graph


def reduction3(graph, k):  # Merge two nodes that are fully connected to the same clique but not connected to each other
    no_changes = True
    while no_changes:  # We repeat this as when merging some nodes different cliques may appear
        cliques = nx.enumerate_all_cliques(graph)
        no_changes = False
        for clique in cliques:
            if len(clique) == k-1 and set(clique).issubset(list(graph.nodes())):  # We iterate over every clique of size k-1 and make sure that it still exists as elements can be merged
                possible_nodes = []
                for i in list(graph.nodes()):
                    if set(clique).issubset(graph.neighbors(i)):
                        possible_nodes.append(i)
                for node1 in range(0, len(possible_nodes)):
                    for node2 in range(node1+1, len(possible_nodes)):
                        if possible_nodes[node1] in graph.nodes() and possible_nodes[node2] in graph.nodes() and possible_nodes[node2] not in graph.neighbors(possible_nodes[node1]):
                            no_changes = True
                            graph = nx.contracted_nodes(graph, possible_nodes[node1], possible_nodes[node2])
    return graph


def reduction(graph, k_colouring):
    graph = reduction1(graph, k_colouring)
    graph = reduction2(graph)
    graph = reduction3(graph, k_colouring)

    return graph
