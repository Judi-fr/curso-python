class Usuario:
    def __init__(self, email, contraseña) -> None:
        self.email = email
        self.contraseña = contraseña

    def encriptar_contraseña(self):  # métodos de instancia
        self.contraseña = self.contraseña[::-1]


user1 = Usuario("juan@mail", "juan123")
user2 = Usuario("admin@mail", "admin123")


lista_usuarios = [user1, user2]
for usuario in lista_usuarios:
    print(f"Email: {usuario.email}\nContraseña: {usuario.contraseña}")
    print()

user1.encriptar_contraseña()
user2.encriptar_contraseña()
print(user1.contraseña)
print(user2.contraseña)
