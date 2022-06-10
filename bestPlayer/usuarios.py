from self import self


class Usuarios():
    numUsuarios = 0
    global users
    users = {}

    def __init__(self, usuario, contraseña, tipoEquipo):
        self.usuario = usuario
        self.contraseña = contraseña
        self.tipoClub = tipoEquipo
        self.conectado = False

        Usuarios.numUsuarios += 1

    def registrarUsuario(self, usuario=None, contraseña=None, confirmarContraseña=None):
        if usuario == None:
            usuario = input("Ingrese su nombre de usuario: \n")
        else:
            usuario = usuario
        if contraseña == None:
            contraseña = input("Ingrese su contraseña: \n")
        else:
            contraseña = contraseña
        if confirmarContraseña == None:
            print("No se pasa contraseña")
            confirmarContraseña = input("Ingrese su contraseña: \n")
        else:
            self.confirmarContraseña = confirmarContraseña
            print(confirmarContraseña)
        if contraseña == confirmarContraseña:
            print("Se ha registrado con éxito")
            user = self.__init__(usuario,contraseña)
            users[user] = contraseña
            return True
        else:
            print("No se ha podido realizar el registro")
            print("Las contraseñas no coinciden")
            return False
            self.registrarUsuario()


    def iniciarSesion(self, usuario=None, contraseña=None):
        if usuario == None:
            usuario = input("Ingrese su nombre de usuario: \n")
        else:
            usuario = usuario
        if contraseña == None:
            contraseña = input("Ingrese su contraseña: \n")
        else:
            contraseña = contraseña
        if usuario == usuario and contraseña == contraseña:
            print("Se ha conectado con éxito")
            self.conectado = True
            return True
        else:
            print("Usuario y/o contraseña incorrecto")
            if contraseña != None:
                return False
            self.iniciarSesion()
    def desconectar(self):
        if self.conectado:
            print("Se cerró sesión con éxito")
            self.conectado = False
        else:
            print("Ya está desconectado")

    def __str__(self):
        if self.conectado:
            connect = "conectado"
        else:
            connect = "desconectado"
        return f"Mi nombre es {self.usuario} y estoy {connect}"