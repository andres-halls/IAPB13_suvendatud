'''
Kodutoo 18
25.11.2014
Andres Liiver
'''

from matplotlib import pyplot as plt
import networkx as nx

def bfs1(source, target, graph):
    queue = set([source])
    nodesSearched = 0
    
    while True:
        if target in queue: break
        nodesSearched += 1
        node = queue.pop()
        queue |= set(graph[node])

    return nodesSearched

def bfs2(source, target, graph):
    pass

def bfs3(source, target, graph):
    pass

def main():
    G = nx.fast_gnp_random_graph(12, 0.25, 142443)
    graph = nx.to_dict_of_lists(G)
    #for x in graph: graph[x] = set(graph[x])
    test1 = bfs1(0, 11, graph)

if __name__ == "__main__":
    main()