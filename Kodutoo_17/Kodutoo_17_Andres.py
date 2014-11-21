'''
Kodutoo 17
21.11.2014
Andres Liiver
'''

from matplotlib import pyplot as plt
import networkx as nx

def main():
    G = nx.fast_gnp_random_graph(50, 0.05, 142443)
    pos = nx.spring_layout(G)
    path = nx.shortest_path(G, source=24, target=43)
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx(G, pos)
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='g')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='g', width=10)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()