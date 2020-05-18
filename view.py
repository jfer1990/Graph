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
        #message = Label(root, text="Click once for create a node, click over two nodes, subsequently to create an edge.")
        #message.pack(side=BOTTOM)
    def getCanvas(self):
        return self.MainCanvas


