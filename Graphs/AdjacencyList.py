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

        if self.vertices == 0:
            return result

        visited = [False for x in range(self.vertices)]

        result, visited = self.bfs_traversal_helper(source, visited)

        for i in range(len(visited)):
            if not visited[i]:
                new_result, visited = self.bfs_traversal_helper(i, visited)
                result += new_result

        return result

    def bfs_traversal_helper(self, source, visited):

        result = ""
        queue = TheQueue()
        queue.enqueue(source)
        visited[source] = True

        while not queue.is_empty():
            r = queue.dequeue()
            result += str(r)
            curr = self.array[r].head
            while curr:
                if not visited[curr.data]:
                    visited[curr.data] = True
                    queue.enqueue(curr.data)
                curr = curr.next

        return result, visited

    def dfs_traversal(self, source):
        # Initiate Result String
        result = ""
        # Keep Track of Number of Vertices
        num_of_vertices = self.vertices

        if num_of_vertices == 0:
            return result

        # Keep track of visited nodes, initiate all indexes to False
        visited = []
        for i in range(num_of_vertices):
            visited.append(False)

        # Begin Depth First Traversal with the starting node, pass in the result string and
        # the visited/processed array
        result, visited = self.dfs_traversal_helper(source, visited)

        # For any nodes who were not part of the previous traversal (Disconnected graph)
        for i in range(num_of_vertices):
            if not visited[i]:
                # Run a new DFS with the new unvisited source and pass in the visited array
                # The result for this specific traversal will be returned as well as updated
                # visited array
                result_new, visited = self.dfs_traversal_helper(i, visited)
                # Final Result
                result += result_new
        # Return Result
        return result

    def dfs_traversal_helper(self, source, visited):
        # Initiate Result String for this traversal
        result = ""

        # Initiate Stack for this traversal
        stack = Stack()
        # Push source onto Stack
        stack.push(source)
        # Updated process array to say it has been visited/placed in stack for future processing
        visited[source] = True

        # Processing the stack
        while not stack.is_empty():
            # Remove from stack
            curr_data = stack.pop()
            # Do what you are supposed to do with the node
            result += str(curr_data)
            # Enter its list of adjacent nodes, starting with the first one

            temp = self.array[curr_data].head

            # Add all adjacent nodes to the stack
            while temp is not None:
                # If this node has not been visited or placed in stack already
                if not visited[temp.data]:
                    # Push onto the stack
                    stack.push(temp.data)
                    # Mark as visited for future processing
                    visited[temp.data] = True
                # Add the next node as well
                temp = temp.next
        # Once entire stack is processed, return the resulting output and the visited array
        return result, visited


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
print("BFS TRAVERSAL")
print(g.bfs_traversal(1))

print("DFS TRAVERSAL")
print(g.dfs_traversal(1))
