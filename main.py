from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        visited = frontier.pop()
        
        for visited not in result:
            result.add(visited)
        
        next = graph[visitedNode]
        next = next.difference(result)
        frontier = frontier.union(next)
        
    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']




def connected(graph):
    allNodes = len(graph)
    
    nodesConnected = reachable(graph, list(graph.keys())[0])
    
    return len(nodesConnected) = allNodes

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False



def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    result = []
    frontier = (set(list(graph.keys)))
    
    while len(frontier) != 0:
        anode = frontier.pop()
        conNode = reachable(graph, node)
        frontier = frontier - connected
        
        result.append(connected)
    return len(result)
    

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2
    
    
    graph = graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    
graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
print("graph: ", graph)
print("reachable test: ", reachable(graph, 'A')))
print("connected test: ", connected(graph))
print("n_components test: ", n_components(graph))
