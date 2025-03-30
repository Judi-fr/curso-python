import tkinter as tk


def mostrar_bienvenida():
    nombre=entrada.get()
    label=tk.Label(app,text=f"Bienvenido, {nombre}!",font=("Times New Roman",12))
    label.place(x=22,y=120)

def crear_entorno():
    app.title("Mi primera app con Tkinter")
    app.geometry("186x170")
    

    label=tk.Label(text="Ingresa tu nombre:", font=("Times New Roman",11))
    label.place(x=37, y=13)

    global entrada
    entrada=tk.Entry(font=("Times New Roman",12),justify="center")
    entrada.place(x=10,y=35)

    boton=tk.Button(app,text="Hola Mundo",font=("Times New Roman",9),command=mostrar_bienvenida,width=10)
    boton.place(x=54,y=67)
app=tk.Tk()
crear_entorno()
app.mainloop()