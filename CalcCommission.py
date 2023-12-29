# Create a window with textbox, label, button widgets
import tkinter as tk
FrmCalc = tk.Tk()
FrmCalc.title("Calculate Commission")
FrmCalc.geometry("250x100")
lblSales = tk.Label(FrmCalc, text = "SALES:")
lblSales.place(x=10, y=10)
lblCommission = tk.Label(FrmCalc, text = "COMMISSION:")
lblCommission.place(x=10, y=35)
txtSales = tk.Entry(FrmCalc, bd=5, justify="center")
txtSales.place(x=110, y=10)
txtCommission = tk.Entry(FrmCalc, bd=5, justify="center")
txtCommission.place(x=110, y=35)
def calculate_Click():
    #pass
    fltCom= float(txtSales.get())*0.15
    txtCommission.delete(0, tk.END)
    txtCommission.insert(0,fltCom)

btncalc= tk.Button(FrmCalc, text="Calculate", command=calculate_Click)
btncalc.place(x=85, y=68)
txtSales.focus()
FrmCalc.mainloop()
