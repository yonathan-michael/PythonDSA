from QueueStructures.TheQueue import TheQueue


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

    def bfs_traversal(self, source):
        result = ""

        # Write - Your - Code
        # For the above graph, it should return "01234" or "02143" etc
        processed = []
        queue = TheQueue()
        queue.enqueue(source)

        while not queue.is_empty():
            r = queue.dequeue()
            result += str(r)
            processed.append(r)
            for index in range(len(self.adjMatrix[r])):
                if index not in processed and self.adjMatrix[r][index] == 1:
                    processed.append(index)
                    queue.enqueue(index)
        return result


def main():
    g = Graph(5)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(1, 4)
    g.add_edge(1, 3)

    g.print_matrix()

    print()
    print()

    print("BFS TRAVERSAL")
    print(g.bfs_traversal(0))


if __name__ == '__main__':
    main()
