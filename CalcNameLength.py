# Import GUI Tkinter module
import tkinter as tk

# import Tkinter messagebox 
from tkinter import messagebox

# create a GUI window
FrmNamelen= tk.Tk()

# Add title and size of window
FrmNamelen.title("Name Length")
FrmNamelen.geometry("300x100")

# create a textbox for user to input a name
txtName= tk.Entry(FrmNamelen,bd=5,justify='center')
txtName.place(x=120,y=30)

# add label for text box
lbltxtName=tk.Label(FrmNamelen, text="Your Name: ")
lbltxtName.place(x=10, y=30)

# define function to calculate name length entered by user 
def calc_Click():

    #create a variable to store name input by user
    sname=txtName.get()

    #calculate length of string 
    intlen= len(sname)
    
    #open a new messagebox with length of user input name
    messagebox.showinfo("Name Length", sname +" is " + str(intlen) + " characters long")
    
# add button to click and calculate length of name
btncalc= tk.Button(FrmNamelen, text="CALCULATE", command=calc_Click)
btncalc.place(x=110, y=70)

#keep cursor on text box
txtName.focus()

 # Show the form window on the screen
FrmNamelen.mainloop()
