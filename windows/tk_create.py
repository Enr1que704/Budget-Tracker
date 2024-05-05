from tkinter import *
from tkinter import ttk

def openCreateWindow(main):
    newWindow = Toplevel(main)
    newWindow.title("Create a new budget")
    newWindow.geometry("600x600")

    # def on_select(event): # handle the selection here
    #     selected_item = combo_box.get()
    #     monthLabel.config(text="Selected Item: " + selected_item)

    year_var = StringVar()
    month_var = StringVar()

    def onSubmit():
        year = year_var.get()
        month = month_var.get()
        
        

        year_var.set("")
        month_var.set("")

    yearLabel = Label(newWindow, text="Year:")
    yearLabel.pack(pady=10)

    yearEntry = Entry(newWindow, textvariable=year_var)
    yearEntry.pack(pady=5)

    monthLabel = Label(newWindow, text="Month:")
    monthLabel.pack(pady=10)

    combo_box = ttk.Combobox(newWindow, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], textvariable=month_var)
    combo_box.pack(pady=5)

    # Set default value
    combo_box.set("January")

    submit = Button(newWindow, text="Submit", command=onSubmit)
    submit.pack(pady=10)

    # Bind event to selection
    # combo_box.bind("<<ComboboxSelected>>", on_select)

    