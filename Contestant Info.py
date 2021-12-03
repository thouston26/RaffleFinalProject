from tkinter import *
import tkinter
import random
import tk as tk
import tkinter as tk


class Data:
    people = []
    x = 0

def empty():
    pass

def pick(n, repeat):
    i = random.randrange(n)
    outputLabel["text"] = Data.people[i]
    if Data.x < repeat:
        root.after(50, pick, n, repeat)
        Data.x += 1
    else:
        Data.x = 0
def run():
    n = len(Data.people)
    if n >= 1:
        pick(n, 100)
    else:

        outputLabel["text"] = "You need at least 1 people."

def run_event(event):
    run()

def add():
    new_person = nameEntry.get()
    if new_person != "":
        Data.people.append(new_person)
        peopleListbox.insert("end", new_person)
    nameText.set("")

def add_event(event):
    add()

root = Tk()

root.title("Raffler")
label = tkinter.Label(root, text = "Choose a Winner!", font=('Arial Bold', 30))
label.pack()
root.geometry('500x350')



nameText = tk.StringVar()
nameEntry = tk.Entry( textvariable=nameText, width=30)
nameEntry.pack()
nameEntry.bind("<Return>", add_event)

nameButton = Button(root, text="Enter", command = add)

nameButton.pack()

emailEntry = Entry(root, width = 40)
emailEntry.pack()
emailEntry.get()

phnEntry = Entry(root, width = 35)
phnEntry.pack()
phnEntry.get()

peopleListbox = tk.Listbox()
peopleListbox.pack(side = "right", fill="y")
peopleListbox.bind("<BackSpace>",)


outputLabel = tk.Label(font=("Roboto", 50))
outputLabel.pack()

root.mainloop()