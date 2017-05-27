#! usr/bin/python
"""This script uses breadth first search to find the shortest path from a 
specified root node to every other node in a connected, undirected, unweighted 
graph. Uses python's Networkx graphs.

NOTE: This is WIP."""

import networkx

class Vertex(object):
    def __init__(self, name, parent_node, height):
        self.name = name
        self.parent_node = parent_node
        self.height = height

    def __repr__(self):
        node = str([self.name, self.parent_node, self.height])
        return node

def breadth_first_search(graph, node):
    """ Traverse a graph breadth first.

    Args:
        graph: Networkx graph. Must be unweighted, undirected and connected.
        node: Root node we will traverse the graph from.
    Returns:
        Subgraph of graph that contains the shortest path from the root_node
        to every other node.
    """
    #TODO: Return exception if graph is not connected, is weighted or directed.
    sub_graph = []
    queue = []
    height = 0
    root_node = Vertex(node, None, height)
    sub_graph.append(root_node)
    queue.append(root_node)
    while len(queue) > 0:
        height += 1
        current_node = queue[0]
        del current_node
        for neighbor in graph.neighbors(current_node.name):
            if neighbor not in [i.name for i in sub_graph]:
                #TODO: Make more efficient way to search sub_graph.
                neighboring_node = Vertex(neighbor, current_node, height)
                queue.append(neighboring_node)
                sub_graph.append(neighboring_node)
    return sub_graph