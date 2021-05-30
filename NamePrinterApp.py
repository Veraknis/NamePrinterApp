from tkinter import *  # From tkinter library, import ALL
root = Tk()  # Need this to create a root for the program to work
root.title('Hello')  # Naming the Gui program
root.geometry("400x400")  # Sizing the Gui program


# Defining a hello func, which creates a label within the root page and prints hello + whatever input was entered by the user into the myTextBox entry widget.
def hello():
    # The Get method is used to return/display the text.
    hello_label = Label(root, text="Hello " + myTextBox.get())
    hello_label.pack()


# Tkinter works off widgets, most items are classed as a widget, a button is one, a text box is one, this is how tkinter works.
myLabel = Label(root, text='Enter your first name: ')
myLabel.pack()  # pack displays the widgit whatever space is avaliable on the specified page. Grid is the more accurate way of telling the program where abouts you want an item to sit on the screen exactly.

myTextBox = Entry(root, width=30)  # Entry method is how inputs are taken.
myTextBox.pack()

# Creating a button which will run our hello function.
myButton = Button(root, text='Submit: ', command=hello)
myButton.pack()

# By calling the root.'mainloop' method the program starts and continuiously runs a loop..
root.mainloop()
# This is how it's able to tell if inputs are made within the program, since this background loop is always running while the program is active.
