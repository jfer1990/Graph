#Code from Tejas Rahane, its github: https://github.com/trahane, and the source of the code : https://stackoverflow.com/users/6009773/trahane
#Modified for Juan Fernando Rodriguez, software engineering student at UADY university.
# may/17/2020
#python 3


from Node import *
from tkinter import *

canvas_width = 1000
canvas_height = 600
sel1 = None
sel2 = None
lista = []



#returns a list of two tuples, containing information about the position of the new nodes painted over the canvas.
def paintNode(evento):
    python_green = "#476042"
    rad = 8
    h, k = (evento.x),(evento.y)
    x1, y1 = (h - rad), (k - rad)
    x2, y2 = (h + rad), (k + rad)
    w.create_oval(x1, y1, x2, y2, fill=python_green)
    return [(h,k,rad)]
def paintEdge(tupla1, tupla2):
    x1, y1 = (tupla1[0]), (tupla1[1])
    x2, y2 = (tupla2[0]), (tupla2[1])
    w.create_line(x1,y1,x2,y2)

#Verify if no other node is before the new one in the same positional coords
def isNewNode(evento):
    radAux = 8
    h, k = (evento.x),(evento.y)
    for each in lista:
        tupla = each[0]
        x1 = float(tupla[0])
        y1 = float(tupla[1])
        rad1 = float(tupla[2])
        distAB = ((x1-h)**2 + (y1-k)**2)**(1/2)
        if distAB <= radAux+rad1:
            return False
    return True

def controller(event):
    global sel1, sel2
    if isNewNode(event):
        lista.append(paintNode(event))
        #refrescar tabla de incidencia de vertices refreshTable()
    else:
        if sel1 == None:
            sel1 = float(event.x),float(event.y)
        elif sel2 == None:
            sel2 = float(event.x),float(event.y)
            paintEdge((sel1),(sel2))
            sel1 = None
            sel2 = None
        else:
            print("error")
        return







master = Tk()
master.title("Points")
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=YES, fill=BOTH)
w.bind("<Button-1>", controller)

message = Label(master, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)

mainloop()