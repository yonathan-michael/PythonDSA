from LinkedLists.SinglyLinkedList import LinkedList


class Graph:
    def __init__(self, vertices):
        # Total Number of Vertices
        self.vertices = vertices

        # Defining a list which can hold multiple Linked Lists
        # equal to the number of vertices in the graph
        self.array = []

        # Creating a new LinkedList for each vertex of the list
        for i in range(vertices):
            # Appending a new LinkedList() on each array index
            self.array.append(LinkedList())

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].prepend(destination)

    def add_vertex(self):
        self.vertices = self.vertices + 1
        self.array.append(LinkedList())

    def remove_edge(self, source, destination):
        for i in range(self.vertices):
            if i == source:
                self.array[i].delete(destination)
                break

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            self.array[i].print_list()


g = Graph(4)

g.add_edge(0, 2)
g.add_edge(0, 1)
g.add_edge(1, 3)
g.add_edge(2, 3)


g.print_graph()

g.remove_edge(0,1)
g.add_vertex()
g.add_vertex()

print()
print()

g.print_graph()