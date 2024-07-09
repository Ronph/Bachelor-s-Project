import pickle
import networkx as nx

from Graph_Reduction import *


rec_depth_counter = 0


def check_colouring_safe(graph, vertex, colours, currentColour):
    for neighbour in list(graph.neighbors(vertex)):
        if neighbour in colours.keys() and colours[neighbour] == currentColour:
            return False
    return True


def graph_rec(graph, colourConstraint, colours, v_index, degree):
    global rec_depth_counter
    rec_depth_counter += 1

    if rec_depth_counter >= 1000000000:  # The recursion cap set at 1 Billion
        return False

    if v_index >= len(graph.nodes):
        return True

    for i in range(1, colourConstraint + 1):

        if check_colouring_safe(graph, degree[v_index], colours, i):
            colours[degree[v_index]] = i

            if graph_rec(graph, colourConstraint, colours, v_index + 1, degree):
                return True

            colours[degree[v_index]] = 0


def check_colouring(graph, colourConstraint, degree):
    colours = {}
    if graph_rec(graph, colourConstraint, colours, 0, degree):
        return True
    return False


def make_plots(colouring, graph_type):
    global rec_depth_counter
    probabilities = []
    rec_depth_list = []
    current_file = 0
    if graph_type == 81:
        for i in range(0, 14):
            solvable_found = 0
            comp_cost = []
            for j in range(1, 11):
                rec_depth_counter = 0
                current_file += 1
                print("We are on graph", current_file)
                path = 'graphs81/graph81_' + str(current_file) + '.pickle'
                G = pickle.load(open(path, 'rb'))
                colouring_val = colouring
                G = reduction(G, colouring_val)

                degree = sorted(G.degree, key=lambda x: x[1], reverse=True)
                degree = [item[0] for item in degree]

                if check_colouring(G, colouring_val, degree):
                    solvable_found += 1
                comp_cost.append(rec_depth_counter)
            rec_depth_list.append(comp_cost)
            probabilities.append(solvable_found * 10)

            current_file = current_file - 10

            solvable_found = 0
            comp_cost = []
            for j in range(1, 11):
                if i == 13:
                    break
                rec_depth_counter = 0
                current_file += 1
                print("We are on graph", current_file)
                path = 'graphs81 and a half/graph81_' + str(current_file) + '.pickle'
                G = pickle.load(open(path, 'rb'))
                colouring_val = colouring
                G = reduction(G, colouring_val)

                degree = sorted(G.degree, key=lambda x: x[1], reverse=True)
                degree = [item[0] for item in degree]

                if check_colouring(G, colouring_val, degree):
                    solvable_found += 1
                comp_cost.append(rec_depth_counter)
            rec_depth_list.append(comp_cost)
            probabilities.append(solvable_found * 10)

            print("The probabilities for avg_conn of", i+1, "\nprobability of:", probabilities,
                  "\nand computation cost of:", rec_depth_list)
            # The print above is to have intermittent "save points" to stop and resume if necessary
            # To resume at a certain point please change the starting file number and the number of loop iterations

        print("\nThe final result:\n", probabilities, "\n", rec_depth_list)

    else:
        for i in range(0, 14):
            solvable_found = 0
            comp_cost = []
            for j in range(1, 11):
                rec_depth_counter = 0
                current_file += 1
                print("We are on graph", current_file)
                path = 'graphs144/graph144_' + str(current_file) + '.pickle'
                G = pickle.load(open(path, 'rb'))
                colouring_val = colouring
                G = reduction(G, colouring_val)

                degree = sorted(G.degree, key=lambda x: x[1], reverse=True)
                degree = [item[0] for item in degree]

                if check_colouring(G, colouring_val, degree):
                    solvable_found += 1
                comp_cost.append(rec_depth_counter)
            rec_depth_list.append(comp_cost)
            probabilities.append(solvable_found * 10)

            current_file = current_file - 10

            solvable_found = 0
            comp_cost = []
            for j in range(1, 11):
                if i == 13:
                    break
                rec_depth_counter = 0
                current_file += 1
                print("We are on graph", current_file)
                path = 'graphs144 and a half/graph144_' + str(current_file) + '.pickle'
                G = pickle.load(open(path, 'rb'))
                colouring_val = colouring
                G = reduction(G, colouring_val)

                degree = sorted(G.degree, key=lambda x: x[1], reverse=True)
                degree = [item[0] for item in degree]

                if check_colouring(G, colouring_val, degree):
                    solvable_found += 1
                comp_cost.append(rec_depth_counter)
            rec_depth_list.append(comp_cost)
            probabilities.append(solvable_found * 10)

            print("The probabilities for avg_conn of", i + 1, "\nprobability of:", probabilities,
                  "\nand computation cost of:", rec_depth_list)
            # The print above is to have intermittent "save points" to stop and resume if necessary
            # To resume at a certain point please change the starting file number and the number of loop iterations

        print("\nThe final result:\n", probabilities, "\n", rec_depth_list)




if __name__ == '__main__':
    colouring = 3  # Change to 4 when necessary
    graph_type = 81  # Change to 144 when necessary
    make_plots(colouring, graph_type)
    # make_plots(colouring, graph_type) will print the array of probabilities (1 to 14 inclusive with a step of 0.5)
    # It will also print the computation cost of all the graphs for the given colouring in the same order as above

    # To note, the main three functions are check_colouring, graph_colouring, and check_colouring_safe. These function
    # are the algorithm. The make_plot function simply ties everything together by calling the reduction operations
    # and iterating through all the graphs.

