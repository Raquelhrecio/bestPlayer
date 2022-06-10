import tkinter
from tkinter import *

import Alineacion
import sparql
from usuarios import Usuarios
from tkinter import messagebox as messages

global user1
user1 = Usuarios("Real Madrid", "1902", "club")
user2 = Usuarios("España", "LaRoja", "seleccion")

usuarioActivo  = user1

class BestPlayer(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        self.config(bg="black")
        self.title("BestPlayer")
        self.iconbitmap('bestPlayer.ico')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        contenedorPrincipal = tkinter.Frame(self, bg="black")
        contenedorPrincipal.grid(padx=40, pady=50, sticky="nsew")
        self.pantallas = dict()

        for F in (
        Acceso, InicioClub, InicioSeleccion, Login, Registro, Plantilla, PantallaAlineacion, Sustitucion, Mercado,
        CrearAlineacion, Seleccionables):  # Aquí se ponen todas las pantallas de la app
            frame = F(contenedorPrincipal, self)  # Aquí se van almacenando las pantallas
            self.pantallas[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(Acceso)  # Aquí se elige el frame que se muestra al iniciar la app

    def showFrame(self, contenedorRequerido):
        frame = self.pantallas[contenedorRequerido]
        frame.tkraise()  # Se trae el frame indicado a primer plano

    pass


class Acceso(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Bienvenido o bienvenida a BestPlayer", font=("Verdana", 24), bg="black", fg="white")
        titulo.pack(pady=20)

        botonIniciarSesion = Button(self, text="Iniciar sesión", font=("Verdana", 24), bg="white", fg="black",
                                    command=lambda: controller.showFrame(Login))
        botonIniciarSesion.pack(pady=50)
        botonIniciarSesion.config(width=20, height=1)

        botonRegistro = Button(self, text="Registrarse", font=("Verdana", 24), bg="white", fg="black",
                               command=lambda: controller.showFrame(Registro))
        botonRegistro.pack(pady=20)
        botonRegistro.config(width=20, height=1)
        pass


class Login(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Inicio de sesión", font=("Verdana", 24), bg="black", fg="white")
        titulo.grid(column=1, row=0)

        nombreLabel = Label(self, text="Nombre: ", bg="Black", fg="White", font=("Verdana", 24))
        nombreLabel.grid(column=0, row=1)

        passLabel = Label(self, text="Contraseña: ", bg="Black", fg="White", font=("Verdana", 24))
        passLabel.grid(column=0, row=2)

        # Entradas de texto
        nombreUsuario = StringVar()
        nombreUsuario.set("")
        nombreEntry = Entry(self, text=nombreUsuario)
        nombreEntry.grid(column=1, row=1)

        passUsuario = StringVar()
        passUsuario.set("")
        passEntry = Entry(self, text=passUsuario, show="*")
        passEntry.grid(column=1, row=2)

        def iniciarSesion():
            test = usuarioActivo.iniciarSesion(nombreUsuario.get(), passUsuario.get())
            if nombreUsuario.get() == " " and passUsuario.get == " ":
                messages.showerror("Error", "Introduzca usuario y contraseña")
            if test:
                messages.showinfo("Conectado", "Se ha iniciado sesión")
                if usuarioActivo.tipoClub == "club":
                    controller.showFrame(InicioClub)
                if usuarioActivo.tipoClub == "seleccion":
                    controller.showFrame(InicioSeleccion)
            else:
                messages.showerror("Error", "Usuario y /o contraseña incorrecto")

        pass

        botonIniciarSesion = Button(self, text="Iniciar sesión", font=("Verdana", 24), bg="white", fg="black",
                                    command=iniciarSesion)
        botonIniciarSesion.grid(column=1, row=3, pady=20)


class InicioClub(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Inicio", font=("Verdana", 24), bg="black", fg="white")
        titulo.pack()

        botonPlantilla = Button(self, text="Plantilla", font=("Verdana", 24), bg="white", fg="black",
                                command=lambda: controller.showFrame(Plantilla))
        botonPlantilla.pack(pady=50)
        botonPlantilla.config(width=20, height=1)

        botonMercado = Button(self, text="Mercado", font=("Verdana", 24), bg="white", fg="black")
        botonMercado.pack(pady=50)
        botonMercado.config(width=20, height=1)
        pass

    pass


class InicioSeleccion(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Inicio", font=("Verdana", 24), bg="black", fg="white")
        titulo.pack(pady=20)

        botonConvocatoria = Button(self, text="Convocatoria", font=("Verdana", 24), bg="white", fg="black",
                                   command=lambda: controller.showFrame(Plantilla))
        botonConvocatoria.pack(pady=50)
        botonConvocatoria.config(width=20, height=1)

        botonSeleccionables = Button(self, text="Seleccionables", font=("Verdana", 24), bg="white", fg="black",
                                     command=lambda: controller.showFrame(Seleccionables))
        botonSeleccionables.pack(pady=20)
        botonSeleccionables.config(width=20, height=1)
        pass

    pass


class Registro(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Registro", font=("Verdana", 24), bg="black", fg="white")
        titulo.grid(column=0, row=0, columnspan=2)

        nombreLabel = Label(self, text="Nombre: ", bg="Black", fg="White", font=("Verdana", 24))
        nombreLabel.grid(column=0, row=1, pady=20)

        passLabel = Label(self, text="Contraseña: ", bg="Black", fg="White", font=("Verdana", 24))
        passLabel.grid(column=0, row=2)

        confirmarPassLabel = Label(self, text="Confirmar contraseña: ", bg="Black", fg="White", font=("Verdana", 24))
        confirmarPassLabel.grid(column=0, row=3)

        # Entradas de texto
        nombreUsuario = StringVar()
        nombreUsuario.set("")
        nombreEntry = Entry(self, text=nombreUsuario)
        nombreEntry.grid(column=1, row=1)

        passUsuario = StringVar()
        passUsuario.set("")
        passEntry = Entry(self, text=passUsuario)
        passEntry.grid(column=1, row=2)

        confirmarPass = StringVar()
        confirmarPass.set("")
        confirmarPassEntry = Entry(self, text=confirmarPass)
        confirmarPassEntry.grid(column=1, row=3)

        def registrarUsuario():
            test = Usuarios.registrarUsuario(nombreUsuario.get(), passUsuario.get(), confirmarPass.get())
            if test:
                messages.showinfo("Registro", "Se ha realizado el registro con éxito")
                if usuarioActivo.tipoClub == "club":
                    controller.showFrame(InicioClub)
                if usuarioActivo.tipoClub == "seleccion":
                    controller.showFrame(InicioSeleccion)
            else:
                messages.showerror("Error", "No se ha podido registrar")

        botonRegistrar = Button(self, text="Registrarse", font=("Verdana", 24), bg="white", fg="black",
                                command=registrarUsuario)
        botonRegistrar.grid(column=1, row=4, pady=20)


class Plantilla(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Plantilla", font=("Verdana", 24), bg="black", fg="white")
        titulo.pack(pady=20)

        botonAlineacion = Button(self, text="Introducir alineación", font=("Verdana", 24), bg="white", fg="black",
                                 command=lambda: controller.showFrame(CrearAlineacion))
        botonAlineacion.pack(pady=50)
        botonAlineacion.config(width=20, height=1)

        botonCambio = Button(self, text="Realizar sustitucion", font=("Verdana", 24), bg="white", fg="black",
                             command=lambda: controller.showFrame(Sustitucion))
        botonCambio.pack(pady=20)
        botonCambio.config(width=20, height=1)

        def inicio():
            if usuarioActivo.tipoClub == "club":
                controller.showFrame(InicioClub)
            if usuarioActivo.tipoClub == "seleccion":
                controller.showFrame(InicioSeleccion)

        botonInicio = Button(self, text="Inicio", font=("Verdana", 24), bg="white", fg="black",
                             command=inicio)
        botonInicio.pack(pady=20)
        botonInicio.config(width=20, height=1)


class PantallaAlineacion(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Crear alineacion", font=("Verdana", 24), bg="black", fg="white")
        titulo.grid(column=0, row=0, columnspan=2)

        botonAlineacion = Button(self, text="Introducir alineación", font=("Verdana", 24), bg="white", fg="black",
                                 command=lambda: controller.showFrame(CrearAlineacion))
        botonAlineacion.grid(column=0, row=2, pady=20)

        botonVolver = Button(self, text="Volver", font=("Verdana", 24), bg="white", fg="black",
                             command=lambda: controller.showFrame(Plantilla))
        botonVolver.grid(column=3, row=3)


class Sustitucion(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Realizar sustitución", font=("Verdana", 24), bg="black", fg="white")
        titulo.pack(pady=20)

        botonVolver = Button(self, text="Volver", font=("Verdana", 24), bg="white", fg="black",
                             command=lambda: controller.showFrame(Plantilla))
        botonVolver.pack(pady=20)
        botonVolver.config(width=20, height=1)


class Mercado(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Mercado", font=("Verdana", 24), bg="black", fg="white")
        titulo.pack(pady=20)

        def busqueda():
            sparql.mercadoMasculino()
            pass

        botonBuscar = Button(self, text="Buscar", font=("Verdana", 24), bg="white", fg="black", command=busqueda)
        botonBuscar.pack(pady=20)
        botonBuscar.config(width=20, height=1)

        botonInicio = Button(self, text="Inicio", font=("Verdana", 24), bg="white", fg="black",
                             command=lambda: controller.showFrame(InicioClub))
        botonInicio.pack(pady=20)
        botonInicio.config(width=20, height=1)

class Seleccionables (tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Seleccionables", font=("Verdana", 24), bg="black", fg="white")
        titulo.pack(pady=20)

        def busqueda():
            # sparql.mercadoMasculino()
            pass

        buscar = Button(self, text="Buscar", font=("Verdana", 24), bg="white", fg="black")
        botonInicio = Button(self, text="Inicio", font=("Verdana", 24), bg="white", fg="black",
                                 command=lambda: controller.showFrame(InicioSeleccion))
        botonInicio.pack(pady=20)
        botonInicio.config(width=20, height=1)


class CrearAlineacion(tkinter.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        titulo = Label(self, text="Crear Alineacion", font=("Verdana", 24), bg="black", fg="white")
        titulo.grid(column=0, row=0, columnspan=2)

        defensas = Label(self, text="Introduzca número de defensas", font=("Verdana", 24), bg="black", fg="white")
        defensas.grid(column=0, row=1)

        numDefensas = IntVar()
        numDefensas.set(0)
        numDefensasEntry = Entry(self, text=numDefensas)
        numDefensasEntry.grid(column=1, row=1)

        medios = Label(self, text="Introduzca número de centrocampistas", font=("Verdana", 24), bg="black", fg="white")
        medios.grid(column=0, row=2)

        numMedios = IntVar()
        numMedios.set(0)
        numMediosEntry = Entry(self, text=numMedios)
        numMediosEntry.grid(column=1, row=2)

        delanteros = Label(self, text="Introduzca número de delanteros", font=("Verdana", 24), bg="black", fg="white")
        delanteros.grid(column=0, row=3)

        numDelanteros = IntVar()
        numDelanteros.set(0)
        numDelanterosEntry = Entry(self, text=numDelanteros)
        numDelanterosEntry.grid(column=1, row=3)


        botonAceptar = Button(self, text="Aceptar", font=("Verdana", 24), bg="white", fg="black")
        botonAceptar.grid(column=0, row=4, pady=100)
        botonAceptar.config(width=20, height=1)

        botonVolver = Button(self, text="Volver", font=("Verdana", 24), bg="white", fg="black",
                             command=lambda: controller.showFrame(Plantilla))
        botonVolver.grid(column=1, row=4, pady=100)
        botonVolver.config(width=20, height=1)


if __name__ == "__main__":
    root = BestPlayer()
    root.mainloop()
