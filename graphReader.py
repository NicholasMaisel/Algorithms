import vertex
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
            print(instructions[index][12:])
            graphAdj[separateGraphCount][instructions[index][11:].replace('\n','')] = []
            # Adds vertex as key in dictionary graphAdj
            index += 1

        elif instructions[index][4:8] == "edge":
            v1, v2 = instructions[index][9:].replace(' ','').split('-')
            # Adds value to list with corresponding key (number of vertex)


            print(graphAdj)
            if v1 in graphAdj[separateGraphCount].keys():   # Checks if there is a key for that node
                graphAdj[separateGraphCount][v1].append(v2) # Adds the second vertex of the edge
            else:
                graphAdj[separateGraphCount][v1] = [v2]

            index += 1
    return(graphAdj)

def main():
    instructions = readFile()
    adjList = follow(instructions)
    matricies = []
    for graph in range(len(adjList)):
        matricies.append(GraphMatrix())
        matricies[graph].makeMatrix(adjList[graph])


main()
