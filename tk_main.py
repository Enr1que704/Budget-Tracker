from tkinter import *
from windows.tk_create import openCreateWindow
from windows.tk_edit import openEditWindow
from windows.tk_view import openViewWindow
from windows.tk_past import openPastWindow

main = Tk(screenName="Main", baseName="Main", className="Main", useTk=1)
main.title("Budget Tracker")
main.geometry("600x600")

def openCreate():
    openCreateWindow(main)

def openView():
    openViewWindow(main)

def openPast():
    openPastWindow(main)

def openEdit():
    openEditWindow(main)

title = Label(main, text="Welcome to the Budget Tracker! Please choose an option below to begin.")
title.pack()

createButton = Button(main, text="Create a new budget", width=20, command=openCreate).pack(pady=5)
viewButton = Button(main, text="View a current budget", width=20, command=openView).pack(pady=5)
pastButton = Button(main, text="View a past budget", width=20, command=openPast).pack(pady=5)
editButton = Button(main, text="Edit a current budget", width=20, command=openEdit).pack(pady=5)
exit = Button(main, text="Exit", command=main.quit).pack(pady=10)

main.mainloop()


