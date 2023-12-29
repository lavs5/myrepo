# Import GUI package 

import tkinter as tk

# create a GUI window
FrmMilestoKm= tk.Tk()

# add title and size of window
FrmMilestoKm.title("Miles to Km Converter")
FrmMilestoKm.geometry("300x150")

# create a textbox for miles input and place in x,y position
txtMiles= tk.Entry(FrmMilestoKm,bd=5,justify='center')
txtMiles.place(x=120,y=30)

# add label for text box and place in x,y position
lbltxtMiles=tk.Label(FrmMilestoKm, text="Miles:")
lbltxtMiles.place(x=10, y=30)

# create a textbox for kilometers input and place in x,y position
txtkm= tk.Entry(FrmMilestoKm,bd=5,justify='center')
txtkm.place(x=120,y=100)

# add label for text box and place in x,y position
lbltxtkm=tk.Label(FrmMilestoKm, text="Kilometers:")
lbltxtkm.place(x=10, y=100)

# define function for calculate command
def convert_Click():

    # multiply by 0.6 to convert miles to km
    fltkm=float(txtMiles.get())*1.609344
    
    # use delete to clear txtkm textbox from previous calculations
    txtkm.delete(0, tk.END)
    
    # insert result in txtkm textbox
    txtkm.insert(0,fltkm)

    # Change background color of km textbox to yellow
    txtkm.config(bg="light green")

# Add a calculate button to convert miles to km to x,y position

btncalc= tk.Button(FrmMilestoKm, text="Convert to Kilometers", command=convert_Click)
btncalc.place(x=100, y=60)

# Keep the cursor on miles textbox
txtMiles.focus()

# Show the form window on the screen
FrmMilestoKm.mainloop()
