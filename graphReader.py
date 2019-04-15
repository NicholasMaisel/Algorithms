import vertex
import Graph

def readFile():
    with open('/Users/nicholasmaisel/Documents/Programming/Algorithms/graphs.txt','r') as graphsFile:
        graphs = graphsFile.readlines()
    return(graphs)


def follow(instructions):
    index = 0
    separateGraphCount = -1
    graphAdj = [] #list of dictionaries representing each graph
    while index < len(instructions):
        print(graphAdj)
        print(instructions[index])
        if instructions[index][:2] == '--':    # Ignores comments
            index += 1

        elif instructions[index][:3] == 'new':
            graphAdj.append({})
            separateGraphCount +=1      #updates which dictionary is holding current graph
            index +=1

        elif instructions[index][4:8] == 'vert':
            print(instructions[index][12:])
            graphAdj[separateGraphCount][instructions[index][11:].replace('\n','')] = []
            index += 1

        elif instructions[index][4:8] == "edge":
            v1, v2 = instructions[index][9:].replace(' ','').split('-')


            print(graphAdj)
            input()
            if v1 in graphAdj[separateGraphCount].keys():   #Checks if there is a key for that node
                graphAdj[separateGraphCount][v1].append(v2) #Adds the second vertex of the edge
            else:
                graphAdj[separateGraphCount][v1] = [v2]

            index += 1
    return(graphAdj)




def main():
    instructions = readFile()
    follow(instructions)

main()
