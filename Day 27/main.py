# def add(*args):
#     print(args[1])
#
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(3, 5, 6, 2, 1, 7, 4, 3))




# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#
#     n =+ kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3,  multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make") # the use of .get() ensures that code does not return an error if the value for self.make is not provided when a new object is initialized.
        self.model = kwargs.get("model") # the use of .get() ensures that code does not return an error if the value for self.model is not provided when a new object is initialized.

my_car = Car(make="Nissan")
print(my_car.model)



from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


my_label.config(text="My_New_Text")

# define a function
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text) # displays when the button is clicked
    print(new_text)

#Buttons
button = Button(text="Click Here", command=button_clicked)
button.pack()


#Entry

input = Entry(width=40)
input.insert(END, string="Some text to begin with.")
input.pack()


#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

def spinbox_used():
        print(spinbox.get())

#Spinbox
spinbox = Spinbox(from_=0, to=100, width=20, command=spinbox_used)
spinbox.pack()

def scale_value(value):
    print(value)

#Scale
scale = Scale(from_=0, to=50, command=scale_value)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()





window.mainloop()
