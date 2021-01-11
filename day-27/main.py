import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
# label.pack(side="left")
label.pack()
label['text'] = "New text"
# OR
label.config(text='New text')


# Button

def button_clicked():
    print("Button clicked!")
    label.config(text=input_field.get())


button = tkinter.Button(text="Click Me!", command=button_clicked)
button.pack()

# Entry
input_field = tkinter.Entry(width=10)
input_field.pack()

window.mainloop()
