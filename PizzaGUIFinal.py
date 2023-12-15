from tkinter import *

# Create a button and associate it with a function to be called when clicked
def on_button_click():

    label.config(text="Option Selected")
def initialwindow(window):
    #Put everything in frame
    frame1 = Frame(window)
    frame1.pack(anchor='n', side=LEFT)
    
   
    #greeting
    greeting = Label(
        master = frame1,
        text="Cassandra's Pizzeria",
        width=20,
        height=5
        )
    greeting.pack()

    #Choose Pizza Heading
    label = Label(frame1, text="Choose Your Pizza")
    label.pack()

    #Create buttons to select pizza type
    pizzaButton(hawaiian, "Hawaiian Pizza", frame1)
    pizzaButton(pepperoni, "Pepperoni Pizza", frame1)
    pizzaButton(cheese, "Cheese Pizza", frame1)
    pizzaButton(custom, "Create a pizza", frame1)

 #add pizza pictures in frame
    frame2 = Frame(window)
    frame2.pack(anchor='n', side=LEFT)
    label=Label(frame2, text="Cassandra's Pizzas")
    label.pack()
    canvaspepperoni = Canvas(frame2,width = 300, height = 300)
    canvaspepperoni.pack()
    img = PhotoImage(file='C:\\Users\\Cassa\Desktop\\Programming Stuff\\Final Project\\resources\\Pepperoni.gif')
    canvaspepperoni.create_image(150, 150, image=img)
    canvashawaiian = Canvas(frame2,width = 300, height = 300)
    canvashawaiian.pack()
    imghawaiian = PhotoImage(file='C:\\Users\\Cassa\Desktop\\Programming Stuff\\Final Project\\resources\\sss.gif')
    canvashawaiian.create_image(150, 150, image=imghawaiian)


    mainloop()

def pizzaButton(callback, buttonText, frame):
    button = Button(master = frame, text=buttonText, command=callback, width = 25, height = 1)
    button.pack(pady=10, padx=20, side=TOP, anchor='w')

def hawaiian(callback, buttonText, frame):
    hawaiibutton = Button(text=buttonText, command=callback, width=25, height=1 )

def pepperoni(callback, buttonText, frame):
    pepperonibutton = Button(text=buttonText, command=callback, width=25, height=1 )
 
def cheese(callback, buttonText, frame):
    cheesebutton = Button(text=buttonText, command=callback, width=25, height=1 )
    
def custom(callback, buttonText, frame):
    custom_window = Toplevel(window)
    custom_window.title("Custom Pizza")
    
    toppings_label = Label(custom_window, text="Select your toppings:")
    toppings_label.pack()

# Create the main Tkinter window
window = Tk()
window.title("Main Window")

# Create a button that, when clicked, opens a new window
open_button = Button(window, text="Open Custom Pizza Window", command=custom)
open_button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
# Create the main window
window = Tk()
window.title("Cassandra's Pizzeria")
initialwindow(window)
#loop window
