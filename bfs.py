from collections import deque
# A class to represent a graph object


class Graph:
    # Constructor
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
    # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

# Function to perform BFS recursively on the graph


def recursiveBFS(graph, q, discovered):
    if not q:
        return
    # dequeue front node and print it
    v = q.popleft()
    print(v, end=' ')
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:
            # mark it as discovered and enqueue it
            discovered[u] = True
            q.append(u)
    recursiveBFS(graph, q, discovered)


if __name__ == '__main__':
    # List of graph edges as per the above diagram
    # edges = [
    # Notice that node 0 is unconnected
    #(1, 8), (1, 5), (1, 2), (8, 6), (8, 4), (8, 3),
    #(6, 10), (6, 7), (2, 9)

    # ]
    edges = list(tuple(map(int, input().split()))
                 for r in range(int(input("Enter edges:"))))
    print(edges)
# total number of nodes in the graph
#n = 11
    n = int(input("Enter value of n:"))
# build a graph from the given edges
    graph = Graph(edges, n)
# to keep track of whether a vertex is discovered or not
    discovered = [False] * n
# create a queue for doing BFS
    q = deque()
# Perform BFS traversal from all undiscovered nodes
    print("\nFollowing is Breadth First Traversal: ")
    for i in range(n):
        if not discovered[i]:
            # mark the source vertex as discovered
            discovered[i] = True
# enqueue source vertex
            q.append(i)
# start BFS traversal from vertex i
            recursiveBFS(graph, q, discovered)
