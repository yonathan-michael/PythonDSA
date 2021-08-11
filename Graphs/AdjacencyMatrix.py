from QueueStructures.TheQueue import TheQueue
from Stacks.Stack import Stack


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

    def bfs_traversal_helper(self, source, visited):
        result = ""
        processed = []
        queue = TheQueue()
        queue.enqueue(source)

        while not queue.is_empty():
            r = queue.dequeue()
            result += str(r)
            processed.append(r)
            visited[r] = True
            for index in range(len(self.adjMatrix[r])):
                if index not in processed and self.adjMatrix[r][index] == 1:
                    processed.append(index)
                    queue.enqueue(index)

        return result, visited

    def bfs_traversal(self, source):
        result = ""

        # Keep Track of Number of Vertices
        num_of_vertices = self.size

        if num_of_vertices == 0:
            return result

        visited = [False for x in range(num_of_vertices)]

        result, visited = self.bfs_traversal_helper(source, visited)

        for i in range(self.size):
            if not visited[i]:
                new_result, visited = self.dfs_traversal_helper(i, visited)
                result += new_result

        return result

    def dfs_traversal(self, source):
        result = ""

        # Keep Track of Number of Vertices
        num_of_vertices = self.size

        if num_of_vertices == 0:
            return result

        visited = []
        for i in range(self.size):
            visited.append(False)

        result, visited = self.dfs_traversal_helper(source, visited)

        for i in range(self.size):
            if not visited[i]:
                new_result, visited = self.dfs_traversal_helper(i, visited)
                result += new_result

        return result

    def dfs_traversal_helper(self, source, visited):
        result = ""
        stack = Stack()
        stack.push(source)
        visited[source] = True

        while not stack.is_empty():
            r = stack.pop()
            result += str(r)
            for index in range(len(self.adjMatrix[r])):
                if index not in visited and self.adjMatrix[r][index] == 1:
                    stack.push(index)
                    visited[index] = True

        return result, visited


def main():
    g = Graph(7)

    g.print_matrix()

    print()
    print()

    g.add_edge(1, 2)
    g.add_edge(1, 3)

    g.add_edge(2, 4)
    g.add_edge(2, 5)

    g.add_edge(3, 6)

    g.print_matrix()

    print()
    print()
    print("BFS TRAVERSAL")
    print(g.bfs_traversal(1))

    print("DFS TRAVERSAL")
    print(g.dfs_traversal(1))


if __name__ == '__main__':
    main()
