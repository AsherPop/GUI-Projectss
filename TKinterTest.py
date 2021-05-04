from tkinter import *

top = Tk()
groceryList = []



def results():
    print(groceryList)


def addToList():
    newValue = E1.get()
    groceryList.append(newValue)


    
#This is a label widget
L1 = Label(top, text = "Grocery List")
L1.grid(column = 0, row = 1)


#This is an entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)


#This is a button widget
B1 = Button(text = "    Print List   ", bg = "red", command = results)
B1.grid(column = 0, row = 3)

B2 = Button(text = "    Add to Your List    ", bg = "green", command = addToList)
B2.grid(column = 1, row = 2)




top.mainLoop()


