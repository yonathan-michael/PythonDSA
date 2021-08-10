class Graph:

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, source, destination):
        self.adjMatrix[source][destination] = 1
        # If undirected than you must do the reverse [destination] to [source]

    def remove_edge(self, source, destination):
        self.adjMatrix[source][destination] = 0
        # If undirected than you must do the reverse [destination] to [source]

    def print_matrix(self):
        i = 0
        for row in self.adjMatrix:
            print(i, end=" -> ")
            i += 1
            for val in row:
                print(val, end=" ")
            print()


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(4, 4)

    g.print_matrix()


if __name__ == '__main__':
    main()
