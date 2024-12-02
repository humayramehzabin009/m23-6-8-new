# Import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add Label 
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)
lbl.pack()  # Ensure the widget is packed

# Add Label for getting name as input from user
name_lbl = Label(text="Full Name", bg="#3895D3")
name_lbl.pack()  # Ensure the widget is packed

# Add Entry for user input
name_entry = Entry()
name_entry.pack()  # Ensure the widget is packed

# Function to display a Message
def display():
    # Read input given by user
    name = name_entry.get().strip()

    # Debugging output: Check the value of 'name'
    print(f"Name entered: {name}")

    if not name:
        # Handle empty input case
        text_box.delete(1.0, END)  # Clear any previous text
        text_box.insert(END, "Please enter your full name!\n")
        return

    # Construct the message
    message = f"Hello {name}!\nWelcome to the Application!\nToday's date is: {date.today()}\n"

    # Debugging output: Check the message being inserted
    print(f"Message displayed: {message}")

    # Display details in the text box
    text_box.delete(1.0, END)  # Clear any previous text
    text_box.insert(END, message)

    # Clear the input field
    name_entry.delete(0, END)

# Add a Text Widget to display information/messages
text_box = Text(height=5, wrap=WORD)
text_box.pack()  # Ensure the widget is packed

# Add button and give value of command as name of the function
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')
btn.pack()  # Ensure the widget is packed

# Run the application
root.mainloop()
