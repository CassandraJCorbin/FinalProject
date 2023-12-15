from tkinter import *
import time

def initialwindow(window):
#variables for photos of pizza
    pepperoniImg = PhotoImage(file='.\\Pepperoni.gif') #image of a pepperoni pizza
    hawaiianImg = PhotoImage(file='.\\Hawaiian.gif') #Image of hawaiian pizza
    #Put everything in frame
    frame1 = Frame(window) #first container, to the left
    frame1.pack(anchor='n', side=LEFT)
#Choose Pizza Heading
    label = Label(frame1, text="Choose Your Pizza")
    label.pack()
#Create buttons to select pizza type
    buttonMaker(defaultCallback, "Hawaiian Pizza", frame1)
    buttonMaker(defaultCallback, "Pepperoni Pizza", frame1)
    buttonMaker(defaultCallback, "Cheese Pizza", frame1)
    buttonMaker(custom, "Create a pizza", frame1)
#add pizza pictures in frame
    frame2 = Frame(window)
    frame2.pack(anchor='n', side=LEFT)
    label=Label(frame2, text="Cassandra's Pizzas")
    label.pack()
#Pepperoni Image
    canvaspepperoni = Canvas(frame2,width = 300, height = 300)
    canvaspepperoni.pack()
    canvaspepperoni.create_image(150, 150, image=pepperoniImg)
#Hawaiian Image
    canvashawaiian = Canvas(frame2,width = 300, height = 300)
    canvashawaiian.pack()
    canvashawaiian.create_image(150, 150, image=hawaiianImg)
#Checkout button
    checkoutButton = Button(master = frame2, text = "Checkout", command = checkout, width = 25, height = 1)
    checkoutButton.pack()
#exit button
    exitButton = Button(master = frame2, text = "Exit", command = quitOut, width = 15, height = 1)
    exitButton.pack()
#run the program
    mainloop()

def buttonMaker(callback, buttonText, frame):
    button = Button(master = frame, text = buttonText, command = callback, width = 25, height = 1)
    button.pack(pady=10, padx=20, side=TOP, anchor='w')

#Pops up when you click a button
def optionSelected():
    popupWindow = Toplevel()
    popupWindow.title("Success")
    optionSelectLabel = Label(popupWindow, text = "Option Selected!\n Please check out")
    optionSelectLabel.pack()

#The function for buttons that aren't custom pizzas
def defaultCallback():
    optionSelected()

#Custom toppings window
def custom():
    customWindow = Toplevel()
    customWindow.title("Select Toppings")
#frame for organzing
    frame1 = Frame(customWindow)
    frame1.pack()
    optionSelectLabel = Label(frame1, text = "Select your toppings:")
    optionSelectLabel.pack()
#checkboxes for toppings
    mushroomsCheck = IntVar()
    sausageCheck = IntVar()
    hamCheck = IntVar()
    baconCheck = IntVar()
    pineappleCheck = IntVar()
    mushroomsCheckBox = Checkbutton(frame1, text = "Mushrooms", variable = mushroomsCheck, onvalue = 1, offvalue = 0)
    mushroomsCheckBox.pack()
    sausageCheckBox = Checkbutton(frame1, text = "Sausage", variable = sausageCheck, onvalue = 1, offvalue = 0)
    sausageCheckBox.pack()
    hamCheckBox = Checkbutton(frame1, text = "Ham", variable = hamCheck, onvalue = 1, offvalue = 0)
    mushroomsCheckBox.pack()
    baconCheckBox = Checkbutton(frame1, text = "Bacon", variable = baconCheck, onvalue = 1, offvalue = 0)
    baconCheckBox.pack()
    pineappleCheckBox = Checkbutton(frame1, text = "Pineapple", variable = pineappleCheck, onvalue = 1, offvalue = 0)
    pineappleCheckBox.pack()


#button callback for checkout
def checkout():
    popupWindow = Toplevel()
    popupWindow.title("Checkout")
    checkOutLabel = Label(popupWindow, text = "Order Received, please pay in store!")
    checkOutLabel.pack()
def quitOut():
    mainWindow.destroy()
# Create the main window
mainWindow = Tk()
mainWindow.title("Cassandra's Pizzeria")
#Run the application
initialwindow(mainWindow)