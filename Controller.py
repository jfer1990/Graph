from view import *
from model import *
from tkinter import *

class Controller:
    def __init__(self, model):
        self.root = Tk()
        self.model = model
        self.view = paintApp(self.root)
        self.w = self.view.MainCanvas
        self.view.MainCanvas.bind("<Button-1>", self.controller)
        self.nodeSelected1 = None

    def run(self):
        self.root.title("Graph viewer")
        self.root.deiconify()
        self.root.mainloop()

        # returns a list of two tuples, containing information about the position of the new nodes painted over the canvas.
    def paintNode(self,node):
        python_green = "#476042"
        rad = node.getRad()
        h, k = (float(node.getPos().getX())), (float(node.getPos().getY()))
        x1, y1 = (h - rad), (k - rad)
        x2, y2 = (h + rad), (k + rad)
        self.w.create_oval(x1, y1, x2, y2, fill=python_green)
        return [(h, k, rad)]

    def paintEdge(self,tupla1, tupla2):
        x1, y1 = (tupla1[0]), (tupla1[1])
        x2, y2 = (tupla2[0]), (tupla2[1])
        w.create_line(x1, y1, x2, y2)


    def controller(self,event):
        aux = Node(Position(event.x,event.y),self.model.hashName())
        nuevoNodo = self.model.addNode(aux) #Si envia True, ya se agregó y creo el nuevo Nodo
        if nuevoNodo == True:
            self.paintNode(aux)
            if self.nodeSelected1 != None:
                print(self.model.createEdge(self.nodeSelected1,aux))
                self.nodeSelected1 = None
            print(self.model.printAdjacentList())
            return True
        elif self.nodeSelected1== None: #Si no se cumple la condición, obtiene el nodo que está ocupado
            self.nodeSelected1 = nuevoNodo
            print(self.model.printAdjacentList())
            return True
        else:
            self.model.createEdge(self.nodeSelected1,nuevoNodo)
            self.nodeSelected1 = None
            print(self.model.printAdjacentList())
            return True
        return False





c = Controller(adjacentList())
c.run()




