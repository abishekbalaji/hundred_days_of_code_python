from tkinter import *

window = Tk()

window.title("First GUI Program")

window.minsize(width=500, height=300)

my_label = Label(text="hello world", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()
my_label["text"] = "New Text"

# OR

my_label.config(text="HeLLLOOOO")

# Button

# def handle_button_click():

button = Button(text="Click Me!", command=lambda: my_label.config(text=inp.get()))
button.pack()

# Entry
inp = Entry(width=10)
inp.focus()

inp.pack()
