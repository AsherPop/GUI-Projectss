from tkinter import *
import random

top = Tk()
playlistList = []
myRolls = []
rollTimes = 0
dieType = 0


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


def week1():
    clearWindow()
    
    L1 = Label(top, text = "Playlist Builder", bg = "gold")
    L1.grid(column = 0, row = 1)

    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    B1 = Button(text = "    Print Your Playlist   ", bg = "LightGoldenRod2", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " + ", bg = "LightGoldenrod2", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "   Export List  ", bg = "LightGoldenrod2", command = exportList)
    B3.grid(column = 0, row = 4)

    BClear = Button(text = "Main Menu", bg = "LightGoldenrod2", command = clearWindow)
    BClear.grid(column = 3, row = 1)


def week2():
    def rollDice():
        #Update variable data
        dieType = E1W2.get()
        rollTimes = E2W2.get()

        #clear window after entry data
        clearWindow()

        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1,int(dieType)))
        
        #display dice rolls and present exit button
        L4W2 = Label(top, text = "Here are your rolls!", bg = "LightGoldenrod2")
        L4W2.grid(column = 0, row = 1)
        
        L5W2 = Label(top, text = "{}".format(myRolls), bg = "LightGoldenrod2")
        L5W2.grid(column = 0, row = 2)
        
        B2W2 = Button(top, text = "Main Menu", bg = "LightGoldenrod2", command = mainMenu)
        B2W2.grid(column = 0, row = 3)
        
    clearWindow()

    L1W2 = Label(top, text = "Dice Roller Program", bg = "gold")
    L1W2.grid(column = 1, row = 1)

    L2W2 = Label(top, text = "How many sides should the die have?", bg = "LightGoldenRod2")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text = "How many times would you like to roll?", bg = "LightGoldenRod2")
    L3W2.grid(column = 2, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)

    B1W2 = Button(text = "Roll!", bg = "LightGoldenrod2", command = rollDice)
    B1W2.grid(column = 1, row = 4)

    #To add: roll function and exit button for main menu
  


if __name__ == "__main__":
    mainMenu()
    top.mainloop()
