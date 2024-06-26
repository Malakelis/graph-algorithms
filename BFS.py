from collections import deque

def bfs(graph, start_vertex):
    visitedList = []
    distance = {vertex: float('inf') for vertex in graph}
    distance[start_vertex] = 0  # Distance from start vertex to itself is 0

    queue = deque(start_vertex)
    visitedList.append(start_vertex)
    while queue:
        current_vertex = queue.popleft()
        for neighbor in graph[current_vertex]:
            if distance[neighbor] == float('inf'):
                queue.append(neighbor)
                if neighbor not in visitedList:
                    visitedList.append(neighbor)
                distance[neighbor] = distance[current_vertex] + 1
    print(visitedList)
    return distance

# Example graph represented as an adjacency list
graph0 = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['B', 'E'],
    'D': ['A', 'B', 'F'],
    'E': ['B', 'C', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['F', 'H'],
    'H': ['G']
}

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

# Running BFS from vertex 'A'
distances = bfs(graph, 'A')
print(distances)
