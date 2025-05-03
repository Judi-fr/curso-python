"""import tkinter as tk


def mostrar_bienvenida():
    nombre = entrada.get()
    bienvenida = tk.Label(app, text=f"¡Bienvenido, {nombre}!", font=("Arial", 18), bg="white", fg="white")
    bienvenida.place(relx=0.5, rely=0.5, anchor="center")


def crear_entorno():
    app.title("Mi primera app con Tkinter")
    app.geometry("600x300")
    app.configure(bg="black")

    label = tk.Label(app, text="Ingresa tu nombre:", font=("Arial", 18), bg="black", fg="white")
    label.place(relx=1.5, rely=1.3, anchor="center")

    global entrada
    entrada = tk.Entry(app, font=("Arial", 18))
    entrada.place(relx=0.5, rely=0.4, anchor="center", width=200, height=25)

    boton = tk.Button(app, text="Enviar", font=("Arial", 14), command=mostrar_bienvenida)
    boton.place(relx=0.5, rely=0.6, anchor="center")


app = tk.Tk()

crear_entorno()

app.mainloop()


print("si, esto esta pasando")
time.sleep(5)
print("si, esto esta pasando")
"""
import time
frase=[" ◎"," ◎ "," ◎ O"," ◎ OS"," ◎ OSS"," ◎ OSS "," ◎ OSS P"," ◎ OSS Po"," ◎ OSS Pow"," ◎ OSS Powe"," ◎ OSS Power"," ◎ OSS Power!"]

lista=[
"▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒",
"▒▒   ▒▒ ▒▒▒     ▒▒▒    ",
"▒▒   ▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒",
"▒▒   ▒▒     ▒▒▒     ▒▒▒",
"▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒",
]

for i in lista:
    print(i)
    time.sleep(0.3) 
for letra in frase:
    print(letra,end="\r")
    time.sleep(0.2)   
print(" ◎ OSS Power!")
