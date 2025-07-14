from tkinter import *


def calculate_distance():
    new_text = entry_box.get()
    km = int(new_text) * 1.60934
    my_label4.config(text=km) # displays when the button is clicked
    print(km)



window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)


#Label
my_label = Label(text="Mile to KM Converter", font=("Arial", 20, "bold"), foreground="green")
my_label.grid(column=1, row=0)


#Entry
entry_box = Entry(text="0", width=50)
entry_box.grid(column=1, row=1)

#Label 2
my_label2 = Label(text="Miles", font=("Arial", 15))
my_label2.grid(column=2, row=1)


#Label 3
my_label3 = Label(text="Is equal to", font=("Arial", 15))
my_label3.grid(column=0, row=2)

#Label 3
my_label3 = Label(text="Km", font=("Arial", 15))
my_label3.grid(column=2, row=2)

#Label 4
my_label4 = Label(text="0", font=("Arial", 15))
my_label4.grid(column=1, row=2)



#Button
button = Button(text="Calculate", font=("Arial", 15), command=calculate_distance)
button.grid(column=1, row=3)






window.mainloop()