



# graph type: dict
# start = vertex
# visited type: set


def dfs(graph, order=None):
    visited = set()  # Keeps track of visited nodes
    prev = {}  # Dictionary to store the predecessor of each node
    pre = {}  # Dictionary to store the previsit number of each node
    post = {}  # Dictionary to store the postvisit number of each node
    clock = 1  # Using a list to keep a reference to the mutable integer

    cc = 1 # connected components counter

    def previsit(node):
        nonlocal clock
        pre[node] = clock
        clock += 1

    def postvisit(node):
        nonlocal clock
        post[node] = clock
        clock += 1

    def explore(node):
        visited.add(node)
        previsit(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                prev[neighbor] = node
                explore(neighbor)
        postvisit(node)

    # default alphabetical order
    if order is None:
        order = reversed(sorted(graph.keys()))
        order = sorted(graph.keys()

        print(order)
    
    for node in order:
        if node not in visited:
            explore(node)
            cc += 1


    return prev, pre, post

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

# Example of using the dfs_explore function
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

graph3 = {

'A' : ['C'],
'B' : ['A', 'D'],
'C' : ['B', 'E', 'F'],
'D' : [],
'E' : ['F', 'G', 'H'],
'F' : ['D'],
'G' : ['H'],
'H' : ['F']
}


graph = graph1

prev, pre, post = dfs(graph, 'A')
prev, pre, post = dfs(graph, 'G')



# zip allows to iterate across two dictionaries
# post not sorted

for (vertex, pre), (vertex2, pre2) in zip(sorted(pre.items()), sorted(post.items())):
    print(vertex + "'s pre is " + str(pre) + ", post is " + str(pre2))



def transpose(graph):
    transposed = {node: [] for node in graph}  # Initialize empty lists for all nodes
    for node in graph:
        for neighbor in graph[node]:
            transposed[neighbor].append(node)  # Reverse the edge
    return transposed

print(graph.keys())







