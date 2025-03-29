import tkinter as tk


def mostrar_bienvenida():
    nombre = entrada.get()
    bienvenida = tk.Label(app, text=f"¡Bienvenido, {nombre}!", font=("Arial", 18), bg="black", fg="white")
    bienvenida.place(relx=0.5, rely=0.5, anchor="center")


def crear_entorno():
    app.title("Mi primera app con Tkinter")
    app.geometry("400x300")
    app.configure(bg="black")

    label = tk.Label(app, text="Ingresa tu nombre:", font=("Arial", 18), bg="black", fg="white")
    label.place(relx=0.5, rely=0.3, anchor="center")

    global entrada
    entrada = tk.Entry(app, font=("Arial", 18))
    entrada.place(relx=0.5, rely=0.4, anchor="center", width=200, height=25)

    boton = tk.Button(app, text="Enviar", font=("Arial", 14), command=mostrar_bienvenida)
    boton.place(relx=0.5, rely=0.6, anchor="center")


app = tk.Tk()

crear_entorno()

app.mainloop()
