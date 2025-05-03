import tkinter as tk

class Calculator:

    def __init__(self,master):
        master.geometry("250x300")
        master.title("Calculadora")
        master.config(bg="#31572c")
        master.resizable(False,False)

        entrada=tk.Entry(text="1",font=("Impact" , 15),fg="#8ac926",bg="#132a13",justify="right")
        entrada.place(x=10,y=10,height=40)


app = tk.Tk()
Calculadora=Calculator(app)
app.mainloop()

#este color para los botones 132a13