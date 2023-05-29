class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):

        x, y = self.find(self.data, '_')
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):

        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):

        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, start, goal):
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        print("Enter the start state matrix \n")
        start = self.accept()
        print("Enter the goal state matrix \n")
        goal = self.accept()
        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)

        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("")
            print("  | ")
            print(" \\\'/\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")

            if (self.h(cur.data, goal) == 0):
                break
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

        self.open.sort(key=lambda x: x.fval, reverse=False)


puz = Puzzle(3)
puz.process()

# This code implements the "8 Puzzle" problem using the A* search algorithm. It consists of two classes: `Node` and `Puzzle`.

# The `Node` class represents a node in the search tree. Each node has a state (`data`), level (depth in the search tree), and a heuristic value (`fval`). The `__init__` method initializes these attributes, and the `generate_child` method generates the child nodes by moving the empty space in different directions. The `shuffle` method swaps the empty space with a neighboring tile to create a new state. The `copy` method creates a deep copy of a state matrix, and the `find` method finds the coordinates of a specific element in the matrix.

# The `Puzzle` class represents the overall puzzle-solving process. The `__init__` method initializes the puzzle's size, open and closed lists. The `accept` method takes input from the user to define the start and goal states. The `f` method calculates the evaluation function `f` for a given node, which is the sum of the heuristic value (`h`) and the level of the node. The `h` method calculates the heuristic value, which in this case is the number of misplaced tiles in the current state compared to the goal state. The `process` method performs the A* search algorithm to find the solution. It initializes the start node, calculates its `f` value, and adds it to the open list. Then, it enters a loop where it selects the node with the lowest `f` value from the open list, generates its child nodes, calculates their `f` values, and adds them to the open list. The current node is moved from the open list to the closed list. This process continues until the goal state is reached. Finally, the solution path is printed.

# To summarize, this code solves the 8 Puzzle problem using the A* search algorithm to find the shortest path from the given start state to the goal state.