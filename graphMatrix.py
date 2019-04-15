from vertex import Vertex

class GraphMatrix:
    def __init__(self):
        self.matrix = []

    def makeMatrix(self, adjacencyList):
        ''' The adjacency list object should be a dictionry of verticies as keys,
        with a list of attached verticies as its value'''

        for i in range(len(adjacencyList)):
            self.matrix.append([])    # Makes a list for each vertex
            for x in range(len(adjacencyList)):
                self.matrix[i].append(0) # Adds zeros to matrix

        for vert in adjacencyList:  # Loops through each vertex
            for connection in adjacencyList[vert]:  # Loops through each adj vertex
                print("VERT, CONNECTION: ", vert, connection)
                self.matrix[int(vert)-1][int(connection)-1] = 1  # Updates the matrix with a connection

        print(self.matrix)
