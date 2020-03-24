def drumMinimGreedy(startNode, finishNode, matrix, n):
    if startNode == finishNode:
        currentNode = -1
    else:
        currentNode = startNode
    visited = []
    drumMinim = 0
    while currentNode != finishNode:
        if currentNode == -1:
            currentNode = startNode
        visited.append(currentNode + 1)
        drum = 9999
        nodMinim = -1
        for i in range(0, n):
            if 0 < matrix[currentNode][i] < drum and i + 1 not in visited:
                drum = matrix[currentNode][i]
                nodMinim = i
        if nodMinim != -1:
            drumMinim += drum
            currentNode = nodMinim
        elif startNode == finishNode:
            #se cauta un ciclu
            #ne intoarcem la primul nod
            drumMinim += matrix[currentNode][startNode]
            currentNode = startNode
        else:
            #nu s-a gasit nodul cautat
            return False
    return drumMinim, visited
