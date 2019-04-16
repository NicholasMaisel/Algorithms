from vertex import Vertex
import Graph
from graphMatrix import GraphMatrix
def readFile():
    with open('/Users/nicholasmaisel/Documents/Programming/Algorithms/graphs.txt','r') as graphsFile:
        graphs = graphsFile.readlines()
    return(graphs)

def follow(instructions):
    index = 0
    separateGraphCount = -1
    graphAdj = [] #list of dictionaries, each dictionary representing each graph
    while index < len(instructions):
        if len(instructions[index].strip()) == 0: # Checks for blank line
            index +=1

        if instructions[index][:2] == '--':    # Ignores comments
            index += 1

        elif instructions[index][:3] == 'new':
            graphAdj.append({})         # Creates new dictionary indicating a separate graph
            separateGraphCount +=1      # Updates which dictionary is holding current graph
            index +=1                   # Moves to next instruction

        elif instructions[index][4:8] == 'vert':

            graphAdj[separateGraphCount][instructions[index][11:].replace('\n','')] = []
            # Adds vertex as key in dictionary graphAdj
            index += 1

        elif instructions[index][4:8] == "edge":
            v1, v2 = instructions[index][9:].replace(' ','').replace('\n','').split('-')
            # Adds value to list with corresponding key (number of vertex)

            if v1 in graphAdj[separateGraphCount].keys():   # Checks if there is a key for that node
                graphAdj[separateGraphCount][v1].append(v2) # Adds the second vertex of the edge
            else:
                graphAdj[separateGraphCount][v1] = [v2]

            index += 1
    return(graphAdj)

def main():
    instructions = readFile()
    MyAdjList = follow(instructions)

    matricies = []
    linkedObjects = []



    for graph in range(len(MyAdjList)):
        linkedObjects.append([])

        # Make graph matricies
        matricies.append(GraphMatrix())
        matricies[graph].makeMatrix(MyAdjList[graph])


        # Make connected objects
        for i in range(len(MyAdjList[graph])):
            linkedObjects[graph].append(0)
            #Creates placeholders

        for vert in MyAdjList[graph].keys():
            linkedObjects[graph][int(vert)-1] = Vertex(vert)
            # Creates Vertex objects and stores them in a list

        for vert in MyAdjList[graph]:
            # add corresponding verticies to adjList of Vertex
            for edge in MyAdjList[graph][vert]:
                linkedObjects[graph][int(vert)-1].addEdge(linkedObjects[graph][int(edge)-1])

#    print(matricies[0].matrix)

    for g in linkedObjects[0]:
        print(g.vid, ": ")
        for i in g.adjList:
            print(i.vid)




main()
