from tkinter import *

top = Tk()
playlistList = []



def results():
    print(playlistList)


def addToList():
    newValue = E1.get()
    playlistList.append(newValue)
    E1.delete(0, END)


def exportList():
    with open('test.txt', 'w') as f:
        for item in playlistList:
            f.write("%s\n" % item)


def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()


def mainMenu():
    clearWindow()
    
    LMain = Label(top, text = "B5 GUI Projects", bg = "gold")
    LMain.grid(column = 2, row = 1)
        
    B1Main = Button(text = "Week 1", bg = "LightGoldenrod2", command = week1)
    B1Main.grid(column = 2, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "LightGoldenrod2", command = week2)
    B2Main.grid(column = 2, row = 3) 

    B3Main = Button(text = "Week 3", bg = "LightGoldenrod2")
    B3Main.grid(column = 2, row = 4)


def week1():
    clearWindow()
    
    L1 = Label(top, text = "Playlist Builder", bg = "gold")
    L1.grid(column = 0, row = 1)


    #Entries
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)


    #Buttons
    B1 = Button(text = "    Print Your Playlist   ", bg = "LightGoldenRod2", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " + ", bg = "LightGoldenrod2", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "   Export List  ", bg = "LightGoldenrod2", command = exportList)
    B3.grid(column = 0, row = 4)

    BClear = Button(text = "Main Menu", bg = "LightGoldenrod2", command = clearWindow)
    BClear.grid(column = 3, row = 1)


def week2():
    clearWindow()

    L1W2 = Label(top, text = "Dice Roller Program", bg = "gold")
    L1W2.grid(column = 1, row = 1)

    L2W2 = Label(top, text = "How many sides should the die have?", bg = "LightGoldenRod2")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text = "How many times would you like to roll", bg = "LightGoldenRod2")
    L3W2.grid(column = 2, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)

    B1W2 = Button(text = "Roll!", bg = "LightGoldenrod2")
    B1W2.grid(column = 1, row = 4)

    #To add: roll function and exit button for main menu
  




if __name__ == "__main__":
    mainMenu()
    top.mainloop()
