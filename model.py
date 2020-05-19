class Node:
    def __init__(self,pos,name):
        self._pos = pos
        self._name = name
        self._rad = 12

    def getPos(self):
        return self._pos
    def getRad(self):
        return self._rad
    def getName(self):
        return self._name
    def setPos(self, pos):
        self._pos = pos



class Position:
    def __init__(self,x,y):
        self._x = x
        self._y = y
    def getX(self):
        return self._x
    def getY(self):
        return self._y


class adjacentList:
    def __init__(self):
        self.nodeList = []
        self.adjList = []
        self._numOfNodes = 0
    def isNewNode(self,node):
        h,k = (node.getPos().getX()),(node.getPos().getY())
        for each in self.nodeList:
            x1 = float(each.getPos().getX())
            y1 = float(each.getPos().getY())
            distAB = ((x1 - h) ** 2 + (y1 - k) ** 2) ** (1 / 2)
            if distAB <= 2*node.getRad():
                return each
        return True

    def getAdjacentList(self):
        return self.adjList


    #Return True if node was added succesfully, otherwise returns False
    def addNode(self,node):
        x = True if self.isNewNode(node) == True else False
        if x:
            self.nodeList.append(node)
            self.adjList.append([node])
            return True
        else:
            return self.isNewNode(node)
    #Precondición: node1 and node2 must be instantiated, returns False when node1 and node2 doesnt already existed
    def createEdge(self,node1, node2):
        pos = -1
        for each in self.nodeList:
            pos += 1
            if each == node1:
                self.adjList[pos] = self.adjList[pos] + [node2]
                return True
        return False
    def printAdjacentList(self):
        c = 0
        output = ""
        for each in self.adjList:
            for elem in self.adjList[c]:
                output = output +" - "+ elem.getName()
            output = output + "\n"
            c += 1
        return output
    def hashName(self):
        val = chr(ord('a')+self._numOfNodes)
        self._numOfNodes += 1
        return val







