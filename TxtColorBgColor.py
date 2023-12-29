# Create GUI window with widgets textbox, button


# Import the GUI package
import tkinter as tk

# Create the GUI application main window 
frmTextClr = tk.Tk()

# Define the title of the window. 
frmTextClr.title("Text Color Demo")

# Define the size of the window
frmTextClr.geometry("200x200")

# Create and place the textbox for user entered text on the parent window
txtclrtext= tk.Entry(frmTextClr, bd=5, justify="center")
txtclrtext.pack(side="top",pady=10)

# Create and place the labels for Text Color and Background Color
lbltxtclr=tk.Label(frmTextClr, text="Text Color")
lbltxtclr.place(x=10, y=50)
lblbgclr= tk.Label(frmTextClr, text="Background Color")
lblbgclr.place(x=85,y=50)

# Function to change textbox foreground property 
def btnblutxt_Click():
    txtclrtext.config(fg="Blue")

# Function to change textbox background property 
def btnYellowBg_Click():
    txtclrtext.config(bg="Yellow")

# Function to change textbox foreground property 
def btnRedTxt_Click():
   txtclrtext.config(fg="Red")

# Function to change textbox background property 
def btnGreenBg_Click():
   txtclrtext.config(bg="Green")

# Create and place the buttons to change text to blue
btnblutxt= tk.Button(frmTextClr, text="Blue Text", command=btnblutxt_Click)
btnblutxt.place(x=10,y=90)

# Create and place the buttons to change background to yellow
btnYellowBG = tk.Button(frmTextClr, text="Yellow Background", command=btnYellowBg_Click)
btnYellowBG.place(x=80, y=90)

# Create and place the buttons to change text to red
btnRedTxt = tk.Button(frmTextClr, text="Red Text", command=btnRedTxt_Click)
btnRedTxt.place(x=10, y=150)

# Create and place the buttons to change background to green
btnGreenBG = tk.Button(frmTextClr, text="Green Background", command=btnGreenBg_Click)
btnGreenBG.place(x=80, y=150)

# Infinite loop of main window
frmTextClr.mainloop()
