import sys
# Find the highest k-core subgraph
# 1- Remove vertices of degree < k -> k'den kucuk elementi olan dict keyini sil
# 2- Until all remaining vertices are connected to each other by degree k or more
# -> her key elementleri her keyi kapsiyor mu kontrol et


def mainFunc(fileName):
    networkDict = {}
    # visitedDict = {}
    parseTxtNetwork(fileName, networkDict)
    # for key in networkDict.keys():
    #     visitedDict[key] = False
    # processNetwork(networkDict, visitedDict)
    findKCores(networkDict)


# def findKCores(networkDict):
#     k = 1
#     flag = True
#     while k > 0:
#         numberOfEdges = 0
#         while flag:
#             flag = False
#             for key in list(networkDict.keys()):
#                 if len(networkDict[key]) < k:
#                     flag = True
#                     for item in networkDict[key]:
#                         networkDict[item].remove(key)
#                     networkDict.pop(key)
#         for key in networkDict.keys():
#             numberOfEdges = numberOfEdges + len(networkDict[key])
#         if numberOfEdges == 0:
#             k = -1
#         else:
#             print(f"For k = {k} there are {len(networkDict.keys())} proteins.")
#             k = k + 1


# def processNetwork(networkDict, visitedDict):
#     k = 1
#     while k > 0:
#         keys = list(networkDict.keys())
#         for key in networkDict.keys():
#             if visitedDict[key] == False:
#                 dfsUtil(key, visitedDict, networkDict, k, keys)
#         returnnum = 0
#         for key in keys:
#             returnnum = returnnum + len(networkDict[key])
#         if returnnum <= 0:
#             k = -1
#         else:
#             print(f"for k = {k} - {returnnum}")
#             print(f"for k = {k} - {len(keys)}")
#             k = k + 1


# def dfsUtil(key, visitedDict, networkDict, k, keys):
#     visitedDict[key] = True
#     for item in networkDict[key]:
#         if len(networkDict[key]) < k:
#             networkDict[item].remove(key)
#             if keys.count(key) > 0:
#                 keys.remove(key)
#         if visitedDict[item] == False:
#             if dfsUtil(item, visitedDict, networkDict, k, keys):
#                 if networkDict[key].count(item) > 0:
#                     networkDict[key].remove(item)
#     return len(networkDict[key]) < k

def findKCores(networkDict: dict):
    k = 1
    degree = {}
    for key in list(networkDict.keys()):
        degree[key] = len(networkDict[key])
    while k > 0:
        visited = []
        numOfEdges = 0
        for key in list(networkDict.keys()):
            if key not in visited:
                recursiveKCores(key, visited, degree, k, networkDict)
        for key in list(networkDict.keys()):
            if degree[key] >= k:
                numOfEdges = numOfEdges + 1
        print(f"For k = {k} there are {numOfEdges} proteins.")
        if numOfEdges == 0:
            k = -1
        else:
            k = k + 1


def recursiveKCores(key, visited, degree, k, networkDict):
    visited.append(key)
    for item in networkDict[key]:
        if degree[key] < k:
            degree[item] = degree[item] - 1
        if item not in visited:
            recursiveKCores(item, visited, degree, k, networkDict)


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
