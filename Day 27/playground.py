from tkinter import *

# define a function
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text) # displays when the button is clicked
    print(new_text)



window = Tk()
window.title("My First GUI Program")
window.minsize(width=1600, height=800)


#Label
my_label = Label(text="I am a Label", font=("Arial", 70, "bold"))
my_label.config(text="Service Dashboard", foreground="green")
my_label.grid(column=3, row=0)
my_label.config(padx=50, pady=50)


#Buttons
button = Button(text="Click Here", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New_Button")
new_button.grid(column=2, row=3)

#Entry
input = Entry(width=40)
input.insert(END, string="Some text to begin with.")
input.grid(column=3, row=2)













window.mainloop()
