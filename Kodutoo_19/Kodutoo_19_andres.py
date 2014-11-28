'''
Kodutoo 19
28.11.2014
Andres Liiver
'''

import networkx as nx
import random

# iterative
def dfs1(graph, source, target):
    S = [source]
    discovered = set()
    nodesSearched = 0

    while S != []:
        node = S.pop()
        if node not in discovered:
            nodesSearched += 1
            discovered.add(node)
            for adjacentNode in graph[node]:
                if adjacentNode not in discovered:
                    S.append(adjacentNode)

    return nodesSearched

# recursive
def dfs2(graph, source, target, _discovered = set()):
    _discovered.add(source)
    nodesSearched = 1

    for node in reversed(graph[source]):
        if node not in _discovered:
            nodesSearched += dfs2(graph, node, target, _discovered)

    return nodesSearched

def main():
    #G_no_path = nx.fast_gnp_random_graph(12, 0.1, 142443)
    #graph_no_path = nx.to_dict_of_lists(G_no_path)
    random.seed()
    print("| algorithm \t| total nodes \t| nodes searched")

    for i in range(3, 10):
        print()
        G = nx.fast_gnp_random_graph(2**i, random.uniform(0.0, 0.5), 142443)
        graph = nx.to_dict_of_lists(G)
        tests1 = []
        tests2 = []

        for n in range(123):
            while True:
                source = random.randrange(0, len(graph)-1)
                target = random.randrange(0, len(graph)-1)
                if source != target: break

            tests1.append(dfs1(graph, source, target))
            tests2.append(dfs2(graph, source, target, set()))

        print("| {0} \t\t| {1} \t\t| {2}".format("dfs1", 2**i, sum(tests1)))
        print("| {0} \t\t| {1} \t\t| {2}".format("dfs2", 2**i, sum(tests2)))

if __name__ == "__main__":
    main()