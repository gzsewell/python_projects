#Zach Sewell
#Adding Make Method
'''This program builds a dictionary where the keys are lables of the verticies. The consecutive integers.'''

class LinkedDirectedGraph:
    INFINITY = "-"

    def __init__(self):
        self.graph = {}

    def add_vertex(self, label):
        self.graph[label] = []

    def add_edge(self, start_label, end_label, weight):
        self.graph[start_label].append((end_label, weight))

    def get_neighbors(self, label):
        return self.graph[label]

    def makeLabelTable(self):
        label_table = {}
        i = 0
        for label in self.graph.keys():
            label_table[label] = i
            i += 1
        return label_table

    def makeDistanceMatrix(self, filename):
        label_table = self.makeLabelTable()
        num_vertices = len(label_table)
        distance_matrix = [[self.INFINITY for x in range(num_vertices)] for y in range(num_vertices)]
        for label in self.graph.keys():
            for neighbor, weight in self.graph[label]:
                distance_matrix[label_table[label]][label_table[neighbor]] = weight
        with open(filename, 'w') as file:
            for row in distance_matrix:
                file.write(' '.join(str(val) for val in row) + '\n')

    def printDistanceMatrix(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip().split()
                print(row)

# Example usage:
g = LinkedDirectedGraph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B", 1)
g.add_edge("A", "C", 2)
g.add_edge("B", "D", 3)
g.add_edge("C", "D", 4)
g.makeDistanceMatrix("distance_matrix.txt")
g.printDistanceMatrix("distance_matrix.txt")
