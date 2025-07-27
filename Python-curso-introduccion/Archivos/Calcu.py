import tkinter as tk

app = tk.Tk()
class Calculator:

    def __init__(self,master):
        master.geometry("250x390")
        master.title("Calculadora")
        master.config(bg="#d8d8d8")
        master.resizable(False,False)



        entrada=tk.Entry(font=("Arial" , 15),fg="#000000",bg="#cec7c7",justify="right")
        
        entrada.grid(row=0,column=0,columnspan=4,sticky="nsew",ipady=22)
        self.CrearBotones()

    def CrearBotones(self):
        botones=(
            ("C",1,0), ("(",1,1), (")",1,2), ("+",1,3),
            ("7",2,0), ("8",2,1), ("9",2,2), (" - ",2,3),
            ("4",3,0), ("5",3,1), ("6",3,2), (" x ",3,3),
            ("1",4,0), ("2",4,1), ("3",4,2), ("%",4,3),
            (". ",5,0),("0",5,1)
        )
        for texto, fila, columna in botones:
            boton = tk.Button(app,padx=23,pady=20,bg="#d8d8d8",fg="#000000",text=texto,
                              command=lambda t=texto: self.boton_click(t)) 
            boton.grid(row=fila,column=columna)
        botonIgual = tk.Button(app,padx=55,pady=20,bg="#d8d8d8",fg="#000000",text="=",
                              command=lambda : self.boton_click("  =  ")) 
        botonIgual.grid(row=5,column=2,columnspan=2)

Calculadora=Calculator(app)
app.mainloop()

#este color para los botones 132a13