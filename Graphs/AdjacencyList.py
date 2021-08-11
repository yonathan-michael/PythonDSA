from LinkedLists.SinglyLinkedList import LinkedList
from QueueStructures.TheQueue import TheQueue
from Stacks.Stack import Stack


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

    def bfs_traversal(self, source):

        result = ""
        processed = []
        queue = TheQueue()
        queue.enqueue(source)

        while not queue.is_empty():
            r = queue.dequeue()
            result += str(r)
            processed.append(r)
            curr = self.array[r].head
            while curr:
                if curr.data not in processed:
                    processed.append(curr.data)
                    queue.enqueue(curr.data)
                curr = curr.next

        return result

    def dfs_traversal(self, source):
        result = ""
        num_of_vertices = self.vertices

        if num_of_vertices == 0:
            return result

        processed = []
        for i in range(num_of_vertices):
            processed.append(False)

        result, processed = self.dfs_traversal_helper(source, processed)

        for i in range(num_of_vertices):
            if not processed[i]:
                result_new, processed = self.dfs_traversal_helper(i, processed)
                result += result_new
        return result


    def dfs_traversal_helper(self, source, processed):
        result = ""

        stack = Stack()
        stack.push(source)
        processed[source] = True

        while not stack.is_empty():
            curr_data = stack.pop()
            result += str(curr_data)

            temp = self.array[curr_data].head

            while temp is not None:
                if not processed[temp.data]:
                    stack.push(temp.data)
                    processed[temp.data] = True
                temp = temp.next
        return result, processed




g = Graph(7)

g.print_graph()

print()
print()

g.add_edge(1, 2)
g.add_edge(1, 3)

g.add_edge(2, 4)
g.add_edge(2, 5)

g.add_edge(3, 6)

g.print_graph()

print()
print()
# print("BFS TRAVERSAL")
# print(g.bfs_traversal(0))

print("DFS TRAVERSAL")
print(g.dfs_traversal(1))
