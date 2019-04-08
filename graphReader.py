def readFile():
    with open('/Users/nicholasmaisel/Documents/Programming/Algorithms/graphs.txt','r') as graphsFile:
        graphs = graphsFile.readlines()
    return(graphs)


def interpret(instructions,flag, instructions):
    index = 0
    while index < len(instructions):
        if instructions[index][:2] == "--":
            pass
        elif instructions[index][:3] == 'new':
            while instructions[index][:3] != 'new':
                #create graph based on graphType
                

        else:
            print("Not Understood.\n\n")



def main():
    instructions = readFile()
    for graphType in ['m','a','l']:     # marks the type to be interpreted
        interpret(instructions, graphType, instructions)
