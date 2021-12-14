from tkinter import *  #Importing all elements Modules needed
import tkinter
import random
import tkinter as tk

#Creating the Class for the list of people to raffle
class Data:
    people = []
    x = 0

def empty():
    pass

#Defining the formula for sorting through the names
def pick(n, repeat):
    i = random.randrange(n)
    outputLabel["text"] = Data.people[i]
    if Data.x < repeat:
        root.after(50, pick, n, repeat)
        Data.x += 1
    else:
        Data.x = 0
#Defiing the run function when the button is pressed
def run():
    n = len(Data.people)
    if n >= 1:
        pick(n, 100)
    else:

        outputLabel["text"] = "You need at least 1 person."

def run_event(event):
    run()

#Defing the add function when the contestants info is entered
def add():
    new_person = [nameEntry.get(), emailEntry.get(), phnEntry.get()] #creating list for info
    if new_person != "":
        Data.people.append(new_person)
        peopleListbox.insert("end", new_person)
    nameText.set("")

def add_event(event):
    add()

#Defining the open function for when the All contestants info button is pressed
def open():
    #creating global variables for the next windo used
    global new_person
    global run_button
    global outputLabel
    top = Toplevel()    #Top level needed to differ between both windows
    top.iconbitmap('lottery-icon-12.ico') #changing Icon
    lbl = Label(top, text="Choose your Winner!", font=('Arial Bold', 30)).pack()
    outputLabel = tk.Label(top, font=("Roboto", 15))
    outputLabel.pack()
    run_button = tk.Button(top, text="RUN", command=run)
    run_button.pack()
    closeButton = Button(top, text= 'Finished', command = top.destroy).pack()  #Button used to close the new window opened

    top.geometry('550x370')



root = Tk()
#Creating main window used for teh program
root.title("Raffler")
root.iconbitmap('lottery-icon-12.ico')
img = tk.PhotoImage(file='randompicker.png') #image used for the header of program
label = tkinter.Label(root, text = "Enter Your Contestants!", font=('Arial Bold', 30))
label.pack()
label["compound"]= tk.TOP,
label["image"] = img
root.geometry('800x650') #Defining the window size



#Variable used for the name
nameText = tk.StringVar()
nameEntry = tk.Entry( textvariable=nameText, width=30)
nameEntry.pack()
nameEntry.insert(0,'Enter Name: ')
nameEntry.bind("<Return>", add_event)

#Variable used for the email
emailEntry = Entry(root, width = 40)
emailEntry.pack()
emailEntry.insert(0,'Enter Email: ')
emailEntry.get()

#Variable used for the phone number
phnEntry = Entry(root, width = 35)
phnEntry.pack()
phnEntry.insert(0,'Enter Phone Number: ')
phnEntry.get()

#Button used to store the name and info in the list and display in list box
nameButton = Button(root, text="Enter Contestant", command = add)
nameButton.pack()

#Listbox used to show what names you have entered for the raffle
peopleListbox = tk.Listbox()
peopleListbox.pack(fill="y",expand = True)
peopleListbox.bind("<BackSpace>",)


#Button used to open next window where you recieve the results
wButton = Button(root, text ="All Contestants Entered", command = open,).pack()

#Variable used for the output of winner or stating whether you have names or not
outputLabel = tk.Label(font=("Roboto", 15))
outputLabel.pack()

root.mainloop()
