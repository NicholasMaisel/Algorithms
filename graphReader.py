from vertex import Vertex
from graphMatrix import GraphMatrix
import DFS
import BFS

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
            for vert2 in MyAdjList[graph][vert]:
                linkedObjects[graph][int(vert)-1].addEdge(linkedObjects[graph][int(vert2)-1])
                linkedObjects[graph][int(vert2)-1].addEdge(linkedObjects[graph][int(vert)-1])


    for g in range(len(linkedObjects)):
        print("\n\nGraph ", g, " BFS Output:")
        print("__________________________")
        if '0' in [x.vid for x in linkedObjects[g]]:
     # Since the last graph is the only graph that starts on vid = 0,
     # This maintains order when printing the traversal results
            BFS.Bfs(linkedObjects[g],'0')
        else:
            BFS.Bfs(linkedObjects[g],'1')


    # Reset Markers
    for g in range(len(linkedObjects)):
        for item in linkedObjects[g]:
            item.unmark()


    for g in range(len(linkedObjects)):
        print("\n\nGraph ", g, " DFS Output:")
        print("__________________________")
        if '0' in [x.vid for x in linkedObjects[g]]:
     # Since the last graph is the only graph that starts on vid = 0,
     # This maintains order when printing the traversal results
            DFS.Dfs(linkedObjects[g],'0')
        else:
            DFS.Dfs(linkedObjects[g],'1')

    for g in range(len(linkedObjects)):
        print("\n\nGraph ", g, " Adjacency List:")
        print("__________________________")
        for i in linkedObjects[g]:
            print(i.vid, [x.vid for x in i.adjList])


    for mat in range(len(matricies)):
        print("\n\nGraph ",mat , " Adjacency Matrix:")
        print('__________________________\n\n\n\n')
        for line in matricies[mat].matrix:
            print(line)














main()
