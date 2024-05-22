
# graph type: dict
# pre type: dict
# post type: dict
# visited type: set

post = {}

def dfs(graph, order = None):
    
    # indiciate we are using global variable
    global post
    
    visited = set()  # Keeps track of visited nodes
    pre = {} 
    post = {}
    prev = {} 
    clock = 1  

    cc = 1 # connected components counter
    ccmap = {}

    def previsit(node):
        nonlocal clock
        pre[node] = clock
        clock += 1

    def postvisit(node):
        nonlocal clock
        post[node] = clock
        clock += 1

    def getNeighbors(graph, node, order=None):
        if order == 'r':
            neighbors = sorted(graph[node], reverse=True)
        elif order is not None:
            neighbors = order
        else:
            neighbors = graph[node]
        return neighbors

    # uses call stack to mimick behavior of stack data structure for DFS
    def explore(node):
        ccmap[node] = cc
        visited.add(node)
        previsit(node)
        neighbors = getNeighbors(graph, node, order=None)
        for neighbor in neighbors:
            if neighbor not in visited:
                prev[neighbor] = node
                explore(neighbor)
        postvisit(node)

    # default alphabetical order, otherwise reversed
    if order is None:
        order = sorted(graph.keys())
    elif order == 'r':
        order = sorted(graph.keys(), reverse=True)
        
    for node in order:
        if node not in visited:
            explore(node)
            cc += 1
            
    return prev, pre, post, ccmap

graph = {
    'A' : ['D', 'G', 'H'],
    'B' : [],
    'C' : ['F'],
    'D' : ['E'],
    'E' : ['A', 'B'],
    'F' : [],
    'G' : [],
    'H' : ['C', 'F']
}

# papadimitriou 3.1
graph1 = {
    'A': ['B', 'E'],
    'B': ['A', 'E'],
    'C' : ['B', 'F'],
    'D' : ['G', 'H'],
    'E' : ['A', 'B', 'F'],
    'F' : ['C', 'E', 'I'],
    'G' : ['D', 'H'],
    'H' : ['D', 'G'],
    'I' : ['F']
}


graph2 = {
    'A': ['B', 'F', 'J'],
    'B': ['A', 'C', 'E'],
    'C': ['B'],
    'D': ['G'],
    'E': ['B', 'I'],
    'F': ['A', 'G'],
    'G': ['D', 'F', 'H'],
    'H': ['G'],
    'I': ['E', 'J'],
    'J': ['A', 'I'],
    'K': ['L'],
    'L': ['K']
}

# example 3 reverse DFS
graph3 = {
    'A' : ['C'],
    'B' : ['A', 'D'],
    'C' : ['B', 'E', 'F'],
    'D' : [],
    'E' : ['F', 'G', 'H', 'A'],
    'F' : ['D'],
    'G' : ['H'],
    'H' : ['F']
}

# hw 2.1
graph0 = {
    'A' : ['D','G'],
    'B' : ['F','G','L'],
    'C' : ['B','E'],
    'D' : ['G','H'],
    'E' : ['A','J'],
    'F' : ['B'],
    'G' : ['H'],
    'H' : ['B', 'L'],
    'I' : ['K'],
    'J' : ['F', 'L'],
    'K' : ['D'],
    'L' : ['E','H','K']
}

graph4 = {
    'A' : ['E'],
    'B' : ['F'],
    'C' : ['G','K'],
    'D' : ['H','I','M','N'],
    'E' : ['A','L'],
    'F' : ['G','J'],
    'G' : ['C'],
    'H' : ['N'],
    'I' : ['N'],
    'J' : ['B'],
    'K' : ['G'],
    'L' : ['A','M'],
    'M' : ['F'],
    'N' : ['C','D']
}


def dfs_print(graph, order = None):
    prev, pre, post, cc = dfs(graph, order=None)
    for (vertex, pre), (vertex2, pre2) in zip((pre.items()), (post.items())):    # if want sorted by letter do sorted pre.items() and post.items()
        print(vertex + "'s pre is " + str(pre) + ", post is " + str(pre2))
    print("Connected Components: " + str(cc))

def transpose(graph):
    transposed = {node: [] for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            transposed[neighbor].append(node)  # Reverse the edge
    return transposed


# scc algorithm
# construct G^R which is transposed graph
# run DFS on tranposed graph and obtain post numbers in descending order (first will be a sink)
# run DFS with that priority to obtain strongly connected components

def SCC(graph):
    graph_transpose = transpose(graph)
    prev, pre, post, cc = dfs(graph_transpose)
    print(post)
    post = sorted(post.keys(), key = post.get, reverse=True) # reverse linearized order by post numbers
    print(post)
    
    prev, pre, post, cc = dfs(graph, order=post)

    # graph print algorithm
    for (vertex, pre), (vertex2, pre2) in zip(sorted(pre.items()), sorted(post.items())):
        print(vertex + "'s pre is " + str(pre) + ", post is " + str(pre2))
    print("Strongly Connected Components: " + str(cc))
    print("Previous pointers " + str(prev))


graph = graph
dfs_print(graph)

#SCC(graph)

#print(transpose(graph))

# r = reversed otherwise none
#dfs_print()

#dfs_print(transpose(graph))