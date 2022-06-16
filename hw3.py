import sys
# Find the highest k-core subgraph
# 1- Remove vertices of degree < k -> k'den kucuk elementi olan dict keyini sil
# 2- Until all remaining vertices are connected to each other by degree k or more
# -> her key elementleri her keyi kapsiyor mu kontrol et


def mainFunc(fileName):
    networkDict = {}
    parseTxtNetwork(fileName, networkDict)
    findKCores(networkDict)


def findKCores(networkDict):
    k = 1
    while k > 0:
        allConnectivityFlag = True
        totalEdges = 0
        for key in list(networkDict.keys()):
            if len(networkDict[key]) < k:
                allConnectivityFlag = False
                for item in networkDict[key]:
                    networkDict[item].remove(key)
                networkDict.pop(key)
            else:
                if all(x in networkDict[key] for x in networkDict.keys()):
                    allConnectivityFlag = False
                totalEdges = totalEdges + len(networkDict[key])
        if totalEdges == 0:
            print(f"For k = {k} there are {totalEdges} proteins.")
            k = -1
        else:
            print(f"For k = {k} there are {totalEdges} proteins.")
            k = k + 1


def parseTxtNetwork(fileName, networkDict):
    for line in open(fileName):
        edge = line.split()
        node1 = edge[0]
        node2 = edge[1]
        if node1 in networkDict.keys():
            networkDict[node1] = networkDict[node1] + [node2]
        else:
            networkDict[node1] = [node2]
        if node2 in networkDict.keys():
            networkDict[node2] = networkDict[node2] + [node1]
        else:
            networkDict[node2] = [node1]


# if len(sys.argv) != 2:
#    print("Less or more arguments.")
# else:
mainFunc("yeast.txt")
