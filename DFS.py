def Dfs(graphList, target):
    target = int(target)-1
    graphList[target].mark()
    print(graphList[target].vid)
    for w in graphList[target].adjList:
        if not w.marked:
            Dfs(graphList,w.vid)
