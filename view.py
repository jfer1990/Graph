#Code from Tejas Rahane, its github: https://github.com/trahane, and the source of the code : https://stackoverflow.com/users/6009773/trahane
#Modified for Juan Fernando Rodriguez, software engineering student at UADY university.
# may/17/2020
#python 3


from tkinter import *


#view
class paintApp():
    def __init__(self,root):

        self.sel1 = None
        self.sel2 = None
        self.lista = []
        self.root = root
        self.root.title("Points")
        self.MainCanvas = Canvas(root, width=1000, height=600)
        self.MainCanvas.pack(expand=YES, fill=BOTH)
        self.message = Label(root, text="Click once for create a node, click over two nodes, subsequently to create an edge.")
        self.message.pack(side=BOTTOM)
        self.ButtonFrame = Frame(self.root,height=4)
        self.ButtonFrame.pack(side = BOTTOM,padx=5,pady=5)
        self.saveButton = Button(self.ButtonFrame,text="Save",height=2,width=6)
        self.BFSButton = Button(self.ButtonFrame, text="BFS", height=2, width=6)
        self.BFSButtonStep = Button(self.ButtonFrame, text="BFS Step-1", height=2, width=6)
        self.saveButton.config(cursor="hand2")
        self.BFSButton.config(cursor="hand2")
        self.BFSButton.pack(side=LEFT)
        self.saveButton.pack(side=LEFT)

        self.nameFile = ""
    def getCanvas(self):
        return self.MainCanvas
    """def openInputWindow(self):
        window = Toplevel(self.root)
        lab = Label(window,text="Introduzca nombre del archivo")
        closeButton = Button(window,text="do save!")
        closeButton.pack(side=BOTTOM)
        lab.pack(side=TOP)
        self.nameFile = StringVar()
        entry = Entry(window,textvariable=self.nameFile)
        entry.pack()
        closeButton.bind("<Button-1>",print(self.nameFile.get()))


        window.mainloop()
        """
    #Precondicion, adjacentList debe ser un diccionario

    def windowAdjacent(self,adjacentList):
        window = Toplevel(self.root)
        window.title("Adjacency list")
        x = 0
        y = 0

        for key,list in adjacentList.items():
            out = key+" => "
            e = Entry(window, width=0, fg='blue', font=('Arial', 16, 'bold'),justify='left')
            e.grid(sticky=W, row=x, column=1)
            for node in list:
                out = out+node.getName()+" - "
                y +=1
            e.insert(END, out)
            x += 1
            y = 0
    #precondicion: recibe una lista de tuplas(x,y) que representan una lista de aristas.
    def windowBFS(self,arbol):
        window = Toplevel(self.root)
        window.title("BFS PATH")
        despliegue = Canvas(window, width=1000, height=600)
        despliegue.pack()
        for index, tuple in enumerate(arbol):
            self.paintNode(tuple[0],despliegue)
            self.paintNode(tuple[1],despliegue)
            self.paintEdge(tuple[0], tuple[1],despliegue)


    def paintNode(self, node,canvas):
        python_green = node.color
        python_white = "#ffffff"
        rad = node.getRad()
        h, k = (float(node.getPos().getX())), (float(node.getPos().getY()))
        x1, y1 = (h - rad), (k - rad)
        x2, y2 = (h + rad), (k + rad)
        canvas.create_oval(x1, y1, x2, y2, fill=python_green)
        canvas.create_text(h, k, font=("Pursia", 13), text=node.getName(), fill='white')
    def paintEdge(self,node1, node2,canvas):
        x1, y1 = (float(node1.getPos().getX())), (float(node1.getPos().getY()))
        x2, y2 = (float(node2.getPos().getX())), (float(node2.getPos().getY()))
        canvas.create_line(x1, y1, x2, y2)
















