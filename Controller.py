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
        self.view.saveButton.bind("<Button-1>",self.save)
        self.nodeSelected1 = None
        self.nodeSelected2 = None

    def run(self):
        self.root.title("Graph viewer")
        self.root.deiconify()
        self.root.mainloop()

        # returns a list of two tuples, containing information about the position of the new nodes painted over the canvas.
    def paintNode(self,node):
        python_green = "#476042"
        python_white = "#ffffff"
        rad = node.getRad()
        h, k = (float(node.getPos().getX())), (float(node.getPos().getY()))
        x1, y1 = (h - rad), (k - rad)
        x2, y2 = (h + rad), (k + rad)
        self.w.create_oval(x1, y1, x2, y2, fill=python_green)
        self.w.create_text(h,k,font=("Pursia",13),text=node.getName(),fill='white')

        return [(h, k, rad)]

    def paintEdge(self,node1, node2):
        x1, y1 = (float(node1.getPos().getX())), (float(node1.getPos().getY()))
        x2, y2 = (float(node2.getPos().getX())), (float(node2.getPos().getY()))
        self.w.create_line(x1, y1, x2, y2)


    def controller(self,event):
        aux = Node(Position(event.x,event.y),self.model.nodeName())
        nuevoNodo = self.model.addNode(aux) #Si envia True, ya se agregó y creo el nuevo Nodo
        if nuevoNodo == True:
            self.model.createEdge(None,aux)
            self.paintNode(aux)
            if self.nodeSelected1 != None:
                self.model.createEdge(self.nodeSelected1,aux)
     #           self.model.createEdge(aux, self.nodeSelected1)
                self.paintEdge(self.nodeSelected1,aux)
                self.nodeSelected1 = None
            return True
        elif self.nodeSelected1== None: #Si no se cumple la condición, obtiene el nodo que está ocupado
            self.nodeSelected1 = nuevoNodo
            return True
        else:
            self.model.createEdge(self.nodeSelected1,nuevoNodo)
    #        self.model.createEdge(nuevoNodo,self.nodeSelected1)
            self.paintEdge(nuevoNodo,self.nodeSelected1)
            self.nodeSelected1 = None
            return True
        return False
    def save(self,event):
        f = open("listaAdyacencia.txt", "w+")
        print(self.model.getAdjacentList())
        f.write(self.model.printAdjacentList())
        self.view.windowAdjacent(self.model.getAdjacentList())






c = Controller(Graphs())
c.run()




