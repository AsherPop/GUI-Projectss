from tkinter import *

top = Tk()
groceryList = []



def results():
    print(playlistList)


def addToList():
    newValue = E1.get()
    playlistList.append(newValue)
    E1.delete(0, END)


    
#Labels
L1 = Label(top, text = "Playlist Builder")
L1.grid(column = 0, row = 1)


#Entries
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)


#Buttons
B1 = Button(text = "    Print Your Playlist   ", bg = "blue", command = results)
B1.grid(column = 0, row = 3)

B2 = Button(text = " + ", bg = "red", command = addToList)
B2.grid(column = 1, row = 2)




top.mainLoop()
