# DFS (depth-first serach)
# chengjun @ xifu, fengxiang, baoji 20120803

import networkx as net
import matplotlib.pyplot as plt
import networkx.generators.small
from networkx.algorithms import traversal
import urllib

g = networkx.generators.small.krackhardt_kite_graph()
# BA= net.random_graphs.barabasi_albert_graph(100,1) 
# pos = net.spring_layout(BA)         
# net.draw(BA,pos,with_labels=False,node_size = 30) 
# net.draw(g)
# plt.show()  # using plt to show the network

# print g.number_of_edges()
# print g.number_of_nodes()
# print g.adjacency_list()

# print dict((x, g.neighbors(x)) for x in g.nodes())

'''
Programming The algorithm of Depth-First Traversal
'''
# def DFS_nodes(graph, node, visited=[]):
    # visited.append(node)
    # for neighbor in graph[node]:
        # if not neighbor in visited:
            # DFS_nodes(graph, neighbor, visited)
    # return visited  

# def DFS_edges(graph, node, visited=[], edges=[]):
    # visited.append(node)
    # for ni in graph[node]:
        # if not ni in visited:
            # edges.append((node, ni))
            # DFS_edges(graph, ni, visited, edges)
    # return edges    
    
# print DFS_nodes(g, 2)    # choose node 0 as the starting point
# print DFS_edges(g, 2)
    
'''
DFS in NetworkX 
'''
print list(traversal.dfs_edges(g))
print traversal.dfs_successors(g)
print traversal.dfs_predecessors(g)
tree = traversal.dfs_tree(g)
tree.successors(0)
# tree.succ
net.draw(tree)
plt.show()
    

   

    