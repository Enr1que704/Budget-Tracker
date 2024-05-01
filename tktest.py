from tkinter import *

main = Tk(screenName="Main", baseName="Main", className="Main", useTk=1)
main.title("Budget Tracker")
main.geometry("600x600")

def createWindow():
    newWindow = Toplevel(main)
    newWindow.title("title")
    newWindow.geometry("600x600")

title = Label(main, text="Welcome to the Budget Tracker! Please choose an option below to begin.")
title.pack()

createButton = Button(main, text="Create a new budget", width=20, command=createWindow).pack()
viewButton = Button(main, text="View a current budget", width=20).pack()
pastButton = Button(main, text="View a past budget", width=20).pack()
editButton = Button(main, text="Edit a current budget", width=20).pack()
exit = Button(main, text="Exit", command=main.quit).pack()

main.mainloop()


