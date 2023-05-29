class MST:
    # Number of vertices in the graph
    V = int(input("Enter the vertex: "))

    # A utility function to find the vertex with minimum key value,
    # from the set of vertices not yet included in MST
    def minKey(self, key, mstSet):
        # Initialize min value
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if not mstSet[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v
        return min_index

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent, graph):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", graph[i][parent[i]])

    # Function to construct and print MST for a graph represented using adjacency matrix representation
    def primMST(self, graph):
        # Array to store constructed MST
        parent = [None] * self.V

        # Key values used to pick the minimum weight edge in the cut
        key = [float('inf')] * self.V

        # To represent the set of vertices included in MST
        mstSet = [False] * self.V

        # Initialize all keys as infinite
        key[0] = 0  # Make key 0 so that this vertex is picked as the first vertex
        parent[0] = -1  # First node is always the root of MST

        # The MST will have V vertices
        for _ in range(self.V - 1):
            # Pick the minimum key vertex from the set of vertices not yet included in MST
            u = self.minKey(key, mstSet)

            # Add the picked vertex to the MST Set
            mstSet[u] = True

            # Update key value and parent index of the adjacent vertices of the picked vertex.
            # Consider only those vertices which are not yet included in MST
            for v in range(self.V):
                # graph[u][v] is non-zero only for adjacent vertices of u
                # mstSet[v] is False for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                    parent[v] = u
                    key[v] = graph[u][v]

        # Print the constructed MST
        self.printMST(parent, graph)


# Driver code
if __name__ == '__main__':
    """
    Let us create the following graph
            2    3
        (0)--(1)--(2)
        |   / \   |
       6|  8/   \5 |7
        | /     \ |
        (3)-------(4)
                  9
    """
    t = MST()
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    # Print the solution
    t.primMST(graph)


# The given code demonstrates an implementation of Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph represented using an adjacency matrix. Here's a breakdown of the code:

# The `MST` class is defined to encapsulate the functions related to finding the MST. It has the following methods:

# 1. `minKey(self, key, mstSet)`: This utility function finds the vertex with the minimum key value from the set of vertices not yet included in the MST. It iterates through all the vertices (`self.V`) and checks if the vertex is not in the MST (`not mstSet[v]`) and has a lower key value (`key[v] < min_val`). It returns the index of the vertex with the minimum key.

# 2. `printMST(self, parent, graph)`: This utility function prints the edges and weights of the constructed MST. It iterates from index 1 to `self.V` and prints the parent vertex (`parent[i]`) and the corresponding edge weight (`graph[i][parent[i]]`).

# 3. `primMST(self, graph)`: This function constructs and prints the MST for the given graph. It initializes the `parent` array to store the MST, the `key` array to keep track of the minimum edge weights, and the `mstSet` array to represent the set of vertices included in the MST. The function iterates `self.V - 1` times to add `self.V - 1` edges to the MST. It calls the `minKey` function to find the vertex with the minimum key value (`u`). Then, it adds `u` to the MST set, and updates the `key` and `parent` arrays for the adjacent vertices of `u` that are not yet in the MST. The function uses the adjacency matrix representation of the graph to check for adjacent vertices and updates the key value if the weight of the edge is smaller than the current key value.

# In the `if __name__ == '__main__':` block, a sample graph is created with 5 vertices. The adjacency matrix `graph` represents the weights of the edges between vertices. The `MST` class is instantiated as `t`, and the `primMST` function is called with the graph. It prints the solution, which is the minimum spanning tree of the given graph.

# To summarize, the code uses Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph represented using an adjacency matrix. It starts with a vertex, adds edges to the MST based on the minimum weight, and continues until all vertices are included in the MST. The code then prints the edges and their weights in the constructed MST.