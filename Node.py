class Node:
    def __init__(self,pos):
        self._pos = pos
        self._next = None
        self._back = None
    def getPos(self):
        return self._pos
    def getNext(self):
        return self._next
    def getBack(self):
        return self._back
    def setPos(self, pos):
        self._pos = pos
    def setNext(self,next):
        self._next = next
    def setBack(self,back):
        self._back = back
class Position:
    def __init__(self,x,y):
        self._x = x
        self._y = y
    def getPosition(self):
        return (self._x,self._y)
