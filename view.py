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
        self.saveButton = Button(self.root,text="Save")
        self.saveButton.pack(side=BOTTOM)
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









