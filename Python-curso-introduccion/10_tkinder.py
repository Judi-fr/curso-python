import tkinter as tk


def crear_entorno():
    app.title("Mi primera app con Tkinter")
    app.geometry("400x300")
    label=tk.Label(text="ingresa tu nombre: ", font=("arial",18))
    label.place(x=20, y=20)
    entrada=tk.Entry(font=("Arial",18))
    entrada.place(x=20, y=60,width=200, height=25)

app=tk.Tk()
crear_entorno()
app.mainloop()