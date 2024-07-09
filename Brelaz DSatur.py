import pickle
import networkx as nx
import matplotlib.pyplot as plt


def find_best_sat(satList):
    max_val = len(max(satList, key=len))  # Find the maximum value in the list
    max_index = [i for i, val in enumerate(satList) if len(val) == max_val]  # Get the indexes where max_val occurs
    return max_index


def find_best_degree(indexList, degreeList):
    for i in range(0, len(degreeList)):
        if degreeList[i] in indexList:
            return i

def DSatur(graph):
    degree = sorted(G.degree, key=lambda x: x[1], reverse=True)
    degree = [item[0] for item in degree]

    saturationDegree = [[] for _ in range(len(degree))]
    colours = [i for i in range(0, 150)]
    coloursUsed = []

    while len(degree) > 0:
        max_index = find_best_sat(saturationDegree)  # Find all the nodes with the highest degree saturation
        indexChoice = find_best_degree(max_index, degree)  # Find the node with the highest degree from the list of nodes with the highest degree saturation
        nodeChoice = degree.pop(indexChoice)  # Remove the node of choice

        neighbours = list(nx.all_neighbors(graph, nodeChoice))

        for i in colours:
            if i not in saturationDegree[nodeChoice]:  # We assign it the first colour that it can take without the condition breaking
                graph.nodes[nodeChoice]['color'] = i
                for j in neighbours:  # We then increase the saturation degree and specify the colour of all neighbouring nodes the have NOT yet been coloured
                    if j in degree:
                        saturationDegree[j].append(i)
                if i not in coloursUsed:
                    coloursUsed.append(i)
                saturationDegree[nodeChoice] = []  # We then permanently empty the saturation degree of the current node since it is now coloured
                break

    return coloursUsed, graph






if __name__ == '__main__':
    # For all the graphs:
    '''for i in range(1, 11):
        file = 'graphs/graph' + str(i) + '.pickle'
        G = pickle.load(open(file, 'rb'))

        colours, graph = DSatur(G)

        print("For graph", i, "the colours used are:", colours)

        colourRepartition = {}
        for i in list(graph.nodes()):
            currentColour = graph.nodes[i]['color']
            if currentColour in colourRepartition.keys():
                colourRepartition[currentColour].append(i)
            else:
                colourRepartition[currentColour] = [i]
        print(colourRepartition, '\n')'''


    # Find largest clique
    G = pickle.load(open('graphs81/graph81_80.pickle', 'rb'))
    cliques = nx.enumerate_all_cliques(G)
    print(max(cliques, key=len))

    # For the Test Graph:
    '''G = pickle.load(open('graphs144 and a half/graph144_31.pickle', 'rb'))

    colours, graph = DSatur(G)

    print("The colours used are:", colours)

    colourRepartition = {}
    for i in list(graph.nodes()):
        currentColour = graph.nodes[i]['color']
        if currentColour in colourRepartition.keys():
            colourRepartition[currentColour].append(i)
        else:
            colourRepartition[currentColour] = [i]
    print(colourRepartition)

    nx.draw(graph, with_labels=True)
    plt.show()'''



