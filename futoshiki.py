# Programa 3
# Carlos Eduardo Leiva Medaglia


# ----------------------------------------------------------#
# MODULOS
# ----------------------------------------------------------#
from tkinter import *
from tkinter import messagebox
import random
import pickle
import datetime

# -----------------------------------------------------------#
# CLASES
# -----------------------------------------------------------#
# Variables para la clase de configuracion
lista_con_juegos_facil = [(
    (">", 0, 0), (">", 0, 2), (">", 0, 3),
    ("4", 1, 0), ("2", 1, 4),
    ("4", 2, 2),
    ("<", 3, 3), ("4", 3, 4),
    ("<", 4, 0), ("<", 4, 1)), ((">", 0, 2), (">", 1, 1), ("2", 1, 1),
                                ("4", 1, 3), (">", 2, 2), ("<", 3, 1), ("4", 4, 0), ("<", 4, 0))]

lista_con_juegos_intermedios = [(("4", 0, 4), ("3", 1, 0), ("v", 1, 0), ("1", 1, 1),
                                 ("˄", 1, 1), ("5", 1, 3), ("5", 2, 1), ("˄", 2, 2),
                                 (">", 2, 3), ("5", 3, 2))]

lista_con_juegos_dificiles = [(("4", 0, 1), (">", 0, 1), ("5", 0, 3), ("4", 1, 0), ("2", 1, 4),
                               ("v", 1, 4), ("3", 3, 0), ("v", 3, 1), ("4", 3, 4), ("3", 4, 1), ("1", 4, 3))]

# Clase para la configuracion
class Configuracion:

    def ventana(self, ventana_principal):
        global ventana_configuracion
        global reloj, lista_timer, nivel, lista_nivel, posicion

        reloj = "Si"
        lista_timer = [0, 0, 0]
        nivel = "Facil"
        lista_nivel = lista_con_juegos_facil[random.randint(0, (len(lista_con_juegos_facil) - 1))]
        posicion = "Derecha"

        nivel_texto = StringVar()
        reloj_texto = StringVar()
        posicion_texto = StringVar()

        ventana_configuracion = Toplevel(ventana_principal)
        ventana_configuracion.geometry("500x500")

        self.horas = Label(ventana_configuracion, text="", font=("Arial", "12"))
        self.horas.place(x=260, y=160)

        self.minutos = Label(ventana_configuracion, text="", font=("Arial", "12"))
        self.minutos.place(x=320, y=160)

        self.segundos = Label(ventana_configuracion, text="", font=("Arial", "12"))
        self.segundos.place(x=385, y=160)

        self.Horas = Entry(ventana_configuracion)
        self.Horas.place(x=260, y=200, width=50, height=50)

        self.Minutos = Entry(ventana_configuracion)
        self.Minutos.place(x=325, y=200, width=50, height=50)

        self.Segundos = Entry(ventana_configuracion)
        self.Segundos.place(x=395, y=200, width=50, height=50)

        self.Horas["state"] = "disabled"
        self.Minutos["state"] = "disabled"
        self.Segundos["state"] = "disabled"

        Label(ventana_configuracion, text="CONFIGURACION", font=("Times New Roman", "16")).place(x=0, y=0)

        Label(ventana_configuracion, text="1. Nivel: ", font=("Arial", "12")).place(x=10, y=42)

        self.boton_facil = Radiobutton(ventana_configuracion, text="Facil", variable=nivel_texto, value='Facil',
                                       indicator=0, selectcolor="light green", font=("Arial", "10"),
                                       command=lambda: self.dificultad(nivel_texto.get()))
        self.boton_facil.place(x=80, y=40, width=80)

        Label(ventana_configuracion, text="°", fg="red", font=("Arial", "20")).place(x=165, y=40)

        self.boton_intermedio = Radiobutton(ventana_configuracion, text="Intermedio", variable=nivel_texto,
                                            value="Intermedio", indicator=0, selectcolor="light green",
                                            font=("Arial", "10"), command=lambda: self.dificultad(nivel_texto.get()))
        self.boton_intermedio.place(x=80, y=80, width=80)

        self.boton_dificil = Radiobutton(ventana_configuracion, text="Dificil", variable=nivel_texto, value="Dificil",
                                         indicator=0, selectcolor="light green", font=("Arial", "10"),
                                         command=lambda: self.dificultad(nivel_texto.get()))
        self.boton_dificil.place(x=80, y=120, width=80)

        Label(ventana_configuracion, text="2. Reloj: ", font=("Arial", "12")).place(x=10, y=162)

        self.boton_si = Radiobutton(ventana_configuracion, text="Si", variable=reloj_texto, value="Si", indicator=0,
                                    selectcolor="light green", font=("Arial", "10"),
                                    command=lambda: self.tiempo(reloj_texto.get()))
        self.boton_si.place(x=80, y=160, width=60)

        Label(ventana_configuracion, text="°", fg="red", font=("Arial", "20")).place(x=145, y=160)

        self.boton_no = Radiobutton(ventana_configuracion, text="No", variable=reloj_texto, value="No", indicator=0,
                                    selectcolor="light green", font=("Arial", "10"),
                                    command=lambda: self.tiempo(reloj_texto.get()))
        self.boton_no.place(x=80, y=200, width=60)

        self.boton_timer = Radiobutton(ventana_configuracion, text="Timer", variable=reloj_texto, value="Timer",
                                       indicator=0, selectcolor="light green", font=("Arial", "10"),
                                       command=lambda: self.tiempo(reloj_texto.get()))
        self.boton_timer.place(x=80, y=240, width=60)

        Label(ventana_configuracion, text="3. Posicion en la ventana", font=("Arial", "12")).place(x=10, y=302)

        self.boton_derecha = Radiobutton(ventana_configuracion, text="Derecha", variable=posicion_texto,
                                         value="Derecha", indicator=0, selectcolor="light green", font=("Arial", "10"),
                                         command=lambda: self.posicion_funcion(posicion_texto.get()))
        self.boton_derecha.place(x=200, y=300)

        Label(ventana_configuracion, text="°", fg="red", font=("Arial", "20")).place(x=270, y=300)

        self.boton_izquierda = Radiobutton(ventana_configuracion, text="Izquierda", variable=posicion_texto,
                                           value="Izquierda", indicator=0, selectcolor="light green",
                                           font=("Arial", "10"),
                                           command=lambda: self.posicion_funcion(posicion_texto.get()))
        self.boton_izquierda.place(x=200, y=340)

        self.guardar = Button(ventana_configuracion, text="Guardar", font=("Times New Roman", "12"),
                              command=self.guardar_info, bg="green", fg="black")
        self.guardar.place(x=10, y=400)

        Label(ventana_configuracion, text="LA CONFIGURACION PREDETERMINADA\n TIENE UN CIRCULO ROJO A SU DERECHA",
              font=("Times New Roman", "14"), fg="dark red").place(x=100, y=400)
        Label(ventana_configuracion,
              text="* EN CASO DE ENTRAR A LA\n CONFIGURACION CON UNA\n CONFIGURACION YA GUARDADA\n Y SE VUELVE A GUARDAR\n SIN MARCAR NADA SE GUARDARA\n LA CONFIGURACION PREDETERMINDADA",
              font=("Times New Roman", "11"), fg="red").place(x=188, y=50)

        ventana_configuracion.mainloop()

    def dificultad(self, valor):
        global lista_nivel, nivel
        nivel = valor
        if valor == "Facil":
            lista_nivel = lista_con_juegos_facil[random.randint(0, (len(lista_con_juegos_facil) - 1))]
        elif valor == "Intermedio":
            lista_nivel = lista_con_juegos_intermedios[random.randint(0, (len(lista_con_juegos_intermedios) - 1))]
        else:
            lista_nivel = lista_con_juegos_dificiles[random.randint(0, (len(lista_con_juegos_dificiles) - 1))]

    def tiempo(self, valor):
        global reloj
        reloj = valor
        if valor == "Si" or valor == "No":
            self.Horas["state"] = "disabled"
            self.Minutos["state"] = "disabled"
            self.Segundos["state"] = "disabled"
            self.horas["text"] = ""
            self.minutos["text"] = ""
            self.segundos["text"] = ""
        else:
            self.horas["text"] = "Horas"
            self.minutos["text"] = "Minutos"
            self.segundos["text"] = "Segundos"

            self.Horas["state"] = "normal"
            self.Minutos["state"] = "normal"
            self.Segundos["state"] = "normal"

            self.Horas.bind("<KeyRelease>", self.horas_funcion)
            self.Minutos.bind("<KeyRelease>", self.minutos_funcion)
            self.Segundos.bind("<KeyRelease>", self.segundos_funcion)

    def horas_funcion(self, *args):
        global lista_timer
        horas_variable = self.Horas.get()
        try:
            horas_variable = int(horas_variable)
            if 0 > horas_variable or horas_variable > 2:
                messagebox.showwarning(title="", message=" ERROR LAS HORAS DEBEN SER UN NUMERO ENTERO ENTRE 0 Y 2")
                self.Horas.delete(0, END)
            else:
                lista_timer[0] = horas_variable
        except:
            messagebox.showwarning(title="", message="ERROR DEBE SER UN NUMERO ENTERO")
            self.Horas.delete(0, END)

    def minutos_funcion(self, *args):
        global lista_timer
        minutos_variable = self.Minutos.get()
        try:
            minutos_variable = int(minutos_variable)
            if 0 <= minutos_variable <= 59:
                lista_timer[1] = minutos_variable
            else:
                messagebox.showwarning(title="", message="ERROR LOS MINUTOS DEBEN SER UN ENTERO ENTRE 0 Y 59")
                self.Minutos.delete(0, END)
        except:
            messagebox.showwarning(title="", message="ERROR DEBE SER UN NUMERO ENTERO")
            self.Horas.delete(0, END)

    def segundos_funcion(self, *args):
        global lista_timer
        segundos_variable = self.Segundos.get()
        try:
            segundos_variable = int(segundos_variable)
            if 0 <= segundos_variable <= 59:
                lista_timer[2] = segundos_variable
            else:
                messagebox.showwarning(title="", message="ERROR LOS SEGUNDOS DEBEN SER UN ENTERO ENTRE 0 Y 59")
                self.Segundos.delete(0, END)
        except:
            messagebox.showwarning(title="", message="ERROR DEBE SER UN NUMERO ENTERO")
            self.Horas.delete(0, END)

    def posicion_funcion(self, value):
        global posicion
        posicion = value

    def guardar_info(self):
        self.reloj = reloj
        self.lista_timer = lista_timer
        if self.reloj == "Timer" and self.lista_timer == [0, 0, 0]:
            messagebox.showwarning(title="", message="DEBE LLENAR AL MENOS UNO DE LOS CAMPOS INDICADOS")
        else:
            self.nivel = nivel
            self.lista_nivel = lista_nivel
            self.posicion = posicion
            ventana_configuracion.destroy()


# Clase Juego
# Variables necesarias para la clase

lista_boton_numero_casilla = []


# Clase del juego

class Juego:
    hh = 0
    mm = 0
    ss = 0

    # Metodo para crear la ventana y sus respectivos widgets
    def widgets(self, ventana, configuracion_juego):
        # Se hacen globales las siguientes variables, para que estas funcionen en los siguientes metodos
        global ventana_jugar, nombre, lista_boton_donde_va_restriccion
        # Se intenta hacer la ventana con sus widgets
        try:
            self.cargo = False
            self.lista_botones_casilla = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]]
            # Se crea la ventana y se le da tamaño
            ventana_jugar = Toplevel(ventana)
            ventana_jugar.geometry("620x600")

            # Se agregan distintas etiquetas con informacion para el juego
            Label(ventana_jugar, text="FUTOSHIKI", font=("Georgia", "20"), bg="dark red", fg="White", width=15,
                  height=2).pack()

            Label(ventana_jugar, text="NIVEL", font=("Arial", "11")).place(x=240, y=90)

            # De el objeto de la clase juego se obtiene el nivel que se configuro y asi se puede mostrar en pantalla
            Label(ventana_jugar, text=(str(configuracion_juego.nivel)).upper(), font=("Arial", "11")).place(x=285, y=90)

            Label(ventana_jugar, text="Nombre del jugador: ", font=("Arial", "12")).place(x=10, y=110)

            nombre = Entry(ventana_jugar, width=35, state="normal")
            nombre.place(x=180, y=112)

            # Boton 00 y donde van sus restricciones
            self.boton00 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(0, 0))
            self.boton00.place(x=160, y=140)

            self.label00_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label00_der.place(x=200, y=150)

            self.label00_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label00_abajo.place(x=170, y=182)

            # Boton 01 y donde sus restricciones
            self.boton01 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(0, 1))
            self.boton01.place(x=220, y=140)

            self.label01_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label01_der.place(x=260, y=150)

            self.label01_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label01_abajo.place(x=230, y=182)

            # Boton 02 y donde van sus restricciones

            self.boton02 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(0, 2))
            self.boton02.place(x=280, y=140)

            self.label02_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label02_der.place(x=320, y=150)

            self.label02_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label02_abajo.place(x=290, y=182)
            # Boton 03 y donde van sus restricciones
            self.boton03 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(0, 3))
            self.boton03.place(x=340, y=140)

            self.label03_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label03_der.place(x=380, y=150)

            self.label03_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label03_abajo.place(x=350, y=182)

            # Boton 04 y donde van sus restricciones
            self.boton04 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(0, 4))
            self.boton04.place(x=400, y=140)

            self.label04_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label04_abajo.place(x=410, y=182)

            # Boton 10 y donde van sus restricciones

            self.boton10 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(1, 0))
            self.boton10.place(x=160, y=200)

            self.label10_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label10_der.place(x=200, y=210)

            self.label10_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label10_abajo.place(x=170, y=242)

            # Boton 11 y donde van sus restricciones
            self.boton11 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(1, 1))
            self.boton11.place(x=220, y=200)

            self.label11_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label11_der.place(x=260, y=210)

            self.label11_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label11_abajo.place(x=230, y=242)

            # Boton 12 y donde van sus restricciones
            self.boton12 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(1, 2))
            self.boton12.place(x=280, y=200)

            self.label12_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label12_der.place(x=320, y=210)

            self.label12_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label12_abajo.place(x=290, y=242)

            # Boton 13 y donde van sus restricciones
            self.boton13 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(1, 3))
            self.boton13.place(x=340, y=200)

            self.label13_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label13_der.place(x=380, y=210)

            self.label13_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label13_abajo.place(x=350, y=242)

            # Boton 14 y donde van sus restricciones
            self.boton14 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(1, 4))
            self.boton14.place(x=400, y=200)

            self.label14_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label14_abajo.place(x=410, y=242)

            # Boton 20 y donde van sus restricciones
            self.boton20 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(2, 0))
            self.boton20.place(x=160, y=260)

            self.label20_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label20_der.place(x=200, y=270)

            self.label20_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label20_abajo.place(x=170, y=302)

            # Boton 21 y dnde van sus restricciones
            self.boton21 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(2, 1))
            self.boton21.place(x=220, y=260)

            self.label21_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label21_der.place(x=260, y=270)

            self.label21_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label21_abajo.place(x=230, y=302)

            # Boton 22 y donde van sus restricciones
            self.boton22 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(2, 2))
            self.boton22.place(x=280, y=260)

            self.label22_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label22_der.place(x=320, y=270)

            self.label22_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label22_abajo.place(x=290, y=302)

            # Boton 23 y donde van sus restricciones
            self.boton23 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(2, 3))
            self.boton23.place(x=340, y=260)

            self.label23_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label23_der.place(x=380, y=270)

            self.label23_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label23_abajo.place(x=350, y=302)

            # Boton 24 y donde van sus restricciones
            self.boton24 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(2, 4))
            self.boton24.place(x=400, y=260)

            self.label24_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label24_abajo.place(x=410, y=302)

            # Boton 30 y donde van sus restricciones
            self.boton30 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(3, 0))
            self.boton30.place(x=160, y=320)

            self.label30_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label30_der.place(x=200, y=330)

            self.label30_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label30_abajo.place(x=170, y=362)
            # Boton 31 y donde van sus restricciones
            self.boton31 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(3, 1))
            self.boton31.place(x=220, y=320)

            self.label31_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label31_der.place(x=260, y=330)

            self.label31_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label31_abajo.place(x=230, y=362)

            # Boton 32 y donde van sus restricciones
            self.boton32 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(3, 2))
            self.boton32.place(x=280, y=320)

            self.label32_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label32_der.place(x=320, y=330)

            self.label32_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label32_abajo.place(x=290, y=362)

            # Boton 33 y donde van sus restricciones
            self.boton33 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(3, 3))
            self.boton33.place(x=340, y=320)

            self.label33_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label33_der.place(x=380, y=330)

            self.label33_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label33_abajo.place(x=350, y=362)

            # Boton 34 y donde van sus restricciones
            self.boton34 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(3, 4))
            self.boton34.place(x=400, y=320)

            self.label34_abajo = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label34_abajo.place(x=410, y=362)

            # Boton 40 y donde van sus restricciones
            self.boton40 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(4, 0))
            self.boton40.place(x=160, y=380)

            self.label40_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label40_der.place(x=200, y=390)

            # Boton 41 y donde van sus restricciones
            self.boton41 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(4, 1))
            self.boton41.place(x=220, y=380)

            self.label41_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label41_der.place(x=260, y=390)

            # Boton 42 y donde van sus restricciones
            self.boton42 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(4, 2))
            self.boton42.place(x=280, y=380)

            self.label42_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label42_der.place(x=320, y=390)

            # Boton 43 y donde van sus restricciones
            self.boton43 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(4, 3))
            self.boton43.place(x=340, y=380)

            self.label43_der = Label(ventana_jugar, text="", font=("Arial", "12"))
            self.label43_der.place(x=380, y=390)

            self.boton44 = Button(ventana_jugar, width=4, height=2, bg="light gray",
                                  command=lambda: self.casilla_funcion(4, 4))
            self.boton44.place(x=400, y=380)

            # Creo una lista donde va la restriccion y su fila y columna correspondiente

            lista_boton_donde_va_restriccion = [(0, 0, self.label00_der, self.label00_abajo),
                                                (0, 1, self.label01_der, self.label01_abajo),
                                                (0, 2, self.label02_der, self.label02_abajo),
                                                (0, 3, self.label03_der, self.label03_abajo),
                                                (0, 4, self.label04_abajo),
                                                (1, 0, self.label10_der, self.label10_abajo),
                                                (1, 1, self.label11_der, self.label11_abajo),
                                                (1, 2, self.label12_der, self.label12_abajo),
                                                (1, 3, self.label13_der, self.label13_abajo),
                                                (1, 4, self.label14_abajo),
                                                (2, 0, self.label20_der, self.label20_abajo),
                                                (2, 1, self.label21_der, self.label21_abajo),
                                                (2, 2, self.label22_der, self.label22_abajo),
                                                (2, 3, self.label23_der, self.label23_abajo),
                                                (2, 4, self.label24_abajo),
                                                (3, 0, self.label30_der, self.label30_abajo),
                                                (3, 1, self.label31_der, self.label31_abajo),
                                                (3, 2, self.label32_der, self.label32_abajo),
                                                (3, 3, self.label33_der, self.label33_abajo),
                                                (3, 4, self.label34_abajo),
                                                (4, 0, self.label40_der), (4, 1, self.label41_der),
                                                (4, 2, self.label42_der), (4, 3, self.label43_der)]

            # Con un ciclo for se busca en el objeto de la configuracion las restricciones del nivel
            # Se comparan columnas y filas
            # Dependiendo de la restriccion se coloca en una etiqueta u otra
            for i in configuracion_juego.lista_nivel:
                fila = i[1]
                columna = i[2]
                restriccion = i[0]
                for j in lista_boton_donde_va_restriccion:
                    fila_comparar = j[0]
                    columna_comparar = j[1]
                    if fila == fila_comparar and columna == columna_comparar:
                        if restriccion == "<" or restriccion == ">":
                            j[2]["text"] = restriccion
                        elif len(j) == 3 and (restriccion == "v" or restriccion == "˄"):
                            j[2]["text"] = restriccion
                        elif len(j) == 4 and (restriccion == "v" or restriccion == "˄"):
                            j[3]["text"] = restriccion

            # Dependiendo de como se haya configurado el panel con los numeros se coloca a la derecha o a la izquierda
            # Cuando se crean los botones permanecen desactivados hasta que se inicie el juego
            v = IntVar()

            if configuracion_juego.posicion == "Derecha":
                self.boton_1 = Radiobutton(ventana_jugar, text="1", bg="light blue", state="disabled", variable=v,
                                           value=1, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: self.boton_funcion(v.get()))
                self.boton_1.place(x=540, y=140, width=40, height=40)

                self.boton_2 = Radiobutton(ventana_jugar, text="2", bg="light blue", state="disabled", variable=v,
                                           value=2, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: self.boton_funcion(v.get()))
                self.boton_2.place(x=540, y=200, width=40, height=40)

                self.boton_3 = Radiobutton(ventana_jugar, text="3", bg="light blue", state="disabled", variable=v,
                                           value=3, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: self.boton_funcion(v.get()))
                self.boton_3.place(x=540, y=260, width=40, height=40)

                self.boton_4 = Radiobutton(ventana_jugar, text="4", bg="light blue", state="disabled", variable=v,
                                           value=4, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: self.boton_funcion(v.get()))
                self.boton_4.place(x=540, y=320, width=40, height=40)

                self.boton_5 = Radiobutton(ventana_jugar, text="5", bg="light blue", state="disabled", variable=v,
                                           value=5, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: self.boton_funcion(v.get()))
                self.boton_5.place(x=540, y=380, width=40, height=40)
            else:
                self.boton_1 = Radiobutton(ventana_jugar, text="1", bg="light blue", state="disabled", variable=v,
                                           value=1, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: [self.boton_funcion(v.get())])
                self.boton_1.place(x=80, y=140, width=40, height=40)

                self.boton_2 = Radiobutton(ventana_jugar, text="2", bg="light blue", state="disabled", variable=v,
                                           value=2, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: self.boton_funcion(v.get()))
                self.boton_2.place(x=80, y=200, width=40, height=40)

                self.boton_3 = Radiobutton(ventana_jugar, text="3", bg="light blue", state="disabled", variable=v,
                                           value=3, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: self.boton_funcion(v.get()))
                self.boton_3.place(x=80, y=260, width=40, height=40)

                self.boton_4 = Radiobutton(ventana_jugar, text="4", bg="light blue", state="disabled", variable=v,
                                           value=4, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: self.boton_funcion(v.get()))
                self.boton_4.place(x=80, y=320, width=40, height=40)

                self.boton_5 = Radiobutton(ventana_jugar, text="5", bg="light blue", state="disabled", variable=v,
                                           value=5, indicator=0, activebackground="blue", selectcolor="green",
                                           command=lambda: self.boton_funcion(v.get()))
                self.boton_5.place(x=80, y=380, width=40, height=40)

            # Se crea una lista con el boton de la casilla y su respectiva fila y columna
            self.lista_posicion_boton = [(self.boton00, 0, 0), (self.boton01, 0, 1), (self.boton02, 0, 2),
                                         (self.boton03, 0, 3), (self.boton04, 0, 4),
                                         (self.boton10, 1, 0), (self.boton11, 1, 1), (self.boton12, 1, 2),
                                         (self.boton13, 1, 3), (self.boton14, 1, 4),
                                         (self.boton20, 2, 0), (self.boton21, 2, 1), (self.boton22, 2, 2),
                                         (self.boton23, 2, 3), (self.boton24, 2, 4),
                                         (self.boton30, 3, 0), (self.boton31, 3, 1), (self.boton32, 3, 2),
                                         (self.boton33, 3, 3), (self.boton34, 3, 4),
                                         (self.boton40, 4, 0), (self.boton41, 4, 1), (self.boton42, 4, 2),
                                         (self.boton43, 4, 3), (self.boton44, 4, 4)]

            # Con un ciclo for se busca donde hay restricciones de numeros y asi se coloca en la casilla correspondiente
            for i in configuracion_juego.lista_nivel:
                fila = i[1]
                columna = i[2]
                restriccion = i[0]
                for j in self.lista_posicion_boton:
                    fila_boton = j[1]
                    columna_boton = j[2]
                    boton = j[0]
                    if fila == fila_boton and columna == columna_boton:
                        try:
                            restriccion = int(restriccion)
                        except:
                            pass
                        # El estado del boton pasa a estar deshabilitado ya que este contiene un digito fijo
                        if isinstance(restriccion, int):
                            boton.config(text=restriccion)
                            boton["state"] = "disabled"
                            self.lista_botones_casilla[fila][columna] = (restriccion, columna)

            # Se crean los botones para las distintas opciones del juego, algunos de ellos inician deshabilitados
            self.iniciar_juego = Button(ventana_jugar, text="INICIAR\n JUEGO", bg="red", fg="black",
                                        font=("Times New Roman", "12"), command=self.iniciar_juego_funcion)
            self.iniciar_juego.place(x=20, y=440, width=100, height=50)

            self.borrar_jugada = Button(ventana_jugar, text="BORRAR\n JUGADA", bg="turquoise", fg="black",
                                        font=("Times New Roman", "12"), state="disabled",
                                        command=self.borrar_jugada_funcion)
            self.borrar_jugada.place(x=140, y=440, width=100, height=50)

            self.terminar_juego = Button(ventana_jugar, text="TERMINAR\n JUEGO", bg="#3ed171", fg="black",
                                         font=("Times New Roman", "12"), state="disabled",
                                         command=lambda: self.terminar_juego_funcion(1))
            self.terminar_juego.place(x=260, y=440, width=100, height=50)

            self.borrar_juego = Button(ventana_jugar, text="BORRAR\n JUEGO", bg="#6d9eeb", fg="black",
                                       font=("Times New Roman", "12"), state="disabled",
                                       command=self.borrar_juego_funcion)
            self.borrar_juego.place(x=380, y=440, width=100, height=50)

            self.top_10 = Button(ventana_jugar, text="TOP\n 10", bg="yellow", fg="black",
                                 font=("Times New Roman", "12"), command=self.top_10_funcion)
            self.top_10.place(x=500, y=440, width=100, height=50)

            self.guardar = Button(ventana_jugar, text="GUARDAR JUEGO", font=("Times New Roman", "10"),
                                  command=self.guardar_partida_funcion, state="disabled")
            self.guardar.place(x=280, y=520)

            self.cargar = Button(ventana_jugar, text="CARGAR JUEGO", font=("Times New Roman", "10"),
                                 command=self.cargar_partida_funcion, state="normal")
            self.cargar.place(x=420, y=520)

            self.horas_reloj = Label(ventana_jugar, text="", font=("Arial", "10"))
            self.horas_reloj.place(x=50, y=520)

            self.minutos_reloj = Label(ventana_jugar, text="", font=("Arial", "10"))
            self.minutos_reloj.place(x=110, y=520)

            self.segundos_reloj = Label(ventana_jugar, text="", font=("Arial", "10"))
            self.segundos_reloj.place(x=170, y=520)

            # Si el usuario configuro un timer o un reloj se le muestra en pantalla
            if configuracion_juego.reloj == "Si" or configuracion_juego.reloj == "Timer":
                Label(ventana_jugar, text="Horas", font=("Arial", "10")).place(x=40, y=500)
                Label(ventana_jugar, text="Minutos", font=("Arial", "10")).place(x=100, y=500)
                Label(ventana_jugar, text="Segundos", font=("Arial", "10")).place(x=160, y=500)

                self.horas_reloj["text"] = "00"
                self.minutos_reloj["text"] = "00"
                self.segundos_reloj["text"] = "00"

            ventana_jugar.mainloop()
        except:
            # En caso de que no haya hecho la configuracion le muestra el mensaje correspondiente
            ventana_jugar.destroy()
            messagebox.showwarning(title="", message="DEBE GUARDAR UNA CONFIGURACION PRIMERO")

    # Metodo para iniciar el juegp
    def iniciar_juego_funcion(self):
        if self.cargo:
            pass
        else:
            self.pila_jugadas = []

        if nombre.get() != "":
            nombre.config(state="disabled")
            if configuracion_juego.reloj == "Si":
                self.hh = 0
                self.mm = 0
                self.ss = 0
                self.reloj("start")
            elif configuracion_juego.reloj == "Timer":
                if self.cargo:
                    self.timer("start", self.hh, self.mm, self.ss)
                else:
                    self.hh = configuracion_juego.lista_timer[0]
                    self.mm = configuracion_juego.lista_timer[1]
                    self.ss = configuracion_juego.lista_timer[2]
                    self.timer("start", self.hh, self.mm, self.ss)
            self.cargo = False
            self.nombre_jugador = nombre.get()
            self.boton_1["state"] = "normal"
            self.boton_2["state"] = "normal"
            self.boton_3["state"] = "normal"
            self.boton_4["state"] = "normal"
            self.boton_5["state"] = "normal"
            self.borrar_jugada["state"] = "normal"
            self.terminar_juego["state"] = "normal"
            self.borrar_juego["state"] = "normal"
            self.guardar["state"] = "normal"
            self.cargar["state"] = "disabled"
            self.iniciar_juego["state"] = "disabled"

            for i in self.lista_posicion_boton:
                if i[0]["text"] == "":
                    i[0]["state"] = "normal"
        else:
            messagebox.showwarning(title="", message="DEBE INTRODUCIR UN NOMBRE PRIMERO")

    # Metodos para el manejo del tiempo
    # Metodo para el timer
    # FALTA INDICAR QUE HACER CUANDO TERMINE EL TIMER
    def timer(self, start_stop, h, m, s):
        global contar_timer
        if start_stop == "start":
            tiempo = int(h) * 3600 + int(m) * 60 + int(s)
            tiempo -= 1
            minuto = tiempo // 60
            segundo = tiempo % 60
            hora = 0
            if minuto > 60:
                hora, minuto = (minuto // 60, minuto % 60)
            self.ss = segundo
            self.mm = minuto
            self.hh = hora
            self.horas_reloj.config(text=str(self.hh))
            self.minutos_reloj.config(text=str(self.mm))
            self.segundos_reloj.config(text=str(self.ss))
            contar_timer = self.horas_reloj.after(1000, lambda: self.timer("start", self.hh, self.mm, self.ss))
            ventana_jugar.update()

            if tiempo == 0:
                self.horas_reloj.after_cancel(contar_timer)
                alerta = messagebox.askyesno(title="",
                                             message="TIEMPO EXPIRADO. ¿DESEA CONTINUAR EL MISMO JUEGO (SI O NO)?")
                if alerta:
                    self.hh = configuracion_juego.lista_timer[0]
                    self.mm = configuracion_juego.lista_timer[1]
                    self.ss = configuracion_juego.lista_timer[2]
                    self.reloj("start")
                else:
                    self.terminar_juego_funcion(0)
        elif start_stop == "stop":
            self.ss = 0
            self.mm = 0
            self.hh = 0
            self.horas_reloj.after_cancel(contar_timer)
            self.horas_reloj.config(text=str(self.hh))
            self.minutos_reloj.config(text=str(self.mm))
            self.segundos_reloj.config(text=str(self.ss))
        else:
            self.horas_reloj.after_cancel(contar_timer)
            self.horas_reloj.config(text=str(self.hh))
            self.minutos_reloj.config(text=str(self.mm))
            self.segundos_reloj.config(text=str(self.ss))

    # Metodo para el reloj
    def reloj(self, start_stop):
        global contar_reloj
        if start_stop == "start":
            self.ss += 1
            if self.ss == 59:
                self.ss = 0
                self.mm += 1
                if self.mm == 59:
                    self.mm = 0
                    self.hh += 1
            self.horas_reloj.config(text=str(self.hh))
            self.minutos_reloj.config(text=str(self.mm))
            self.segundos_reloj.config(text=str(self.ss))

            ventana_jugar.update()
            contar_reloj = self.horas_reloj.after(1000, lambda: self.reloj("start"))
        elif start_stop == "stop":
            self.hh = 0
            self.mm = 0
            self.ss = 0
            self.horas_reloj.after_cancel(contar_reloj)
            self.horas_reloj.config(text=str(self.hh))
            self.minutos_reloj.config(text=str(self.mm))
            self.segundos_reloj.config(text=str(self.ss))
        else:
            self.horas_reloj.after_cancel(contar_reloj)
            self.horas_reloj.config(text=str(self.hh))
            self.minutos_reloj.config(text=str(self.mm))
            self.segundos_reloj.config(text=str(self.ss))

    # Metodo para borrar jugadas
    def borrar_jugada_funcion(self):
        if self.pila_jugadas != []:
            ultimo_elemento = self.pila_jugadas[-1]
            fila = ultimo_elemento[1]
            columna = ultimo_elemento[2]
            for fila_comparar, i in enumerate(self.lista_botones_casilla):
                for columna_comparar, j in enumerate(i):
                    if fila == fila_comparar and columna == columna_comparar:
                        self.lista_botones_casilla[fila][columna] = (0, columna)

            self.pila_jugadas.pop()
            elemento = ""
            for i in self.pila_jugadas:
                fila_comparar = i[1]
                columna_comparar = i[2]
                if fila == fila_comparar and columna == columna_comparar:
                    elemento = i[0]
                    self.lista_botones_casilla[fila][columna] = (elemento, columna)

            for i in self.lista_posicion_boton:
                boton = i[0]
                fila_comparar = i[1]
                columna_comparar = i[2]
                if fila == fila_comparar and columna == columna_comparar:
                    boton.config(text=elemento)
        else:
            messagebox.showinfo(title="", message="NO HAY MÁS JUGADAS PARA BORRAR")

    # Metodo para terminar el juego
    def terminar_juego_funcion(self, mostrar_alerta):
        global lista_boton_numero_casilla
        if mostrar_alerta == 1:
            alerta = messagebox.askyesno(title="", message="¿ESTÁ SEGURO DE TERMINAR EL JUEGO (SI o NO)?")
        else:
            alerta = True
        if alerta:
            self.lista_botones_casilla = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]]

            for i in self.lista_posicion_boton:
                i[0].config(text="")

            if configuracion_juego.nivel == "Facil":
                numero = random.randint(0, (len(lista_con_juegos_facil) - 1))
                lista_nivel = lista_con_juegos_facil[numero]
                configuracion_juego.lista_nivel = lista_nivel

            elif configuracion_juego.nivel == "Intermedio":
                numero = random.randint(0, (len(lista_con_juegos_intermedios) - 1))
                lista_nivel = lista_con_juegos_intermedios[numero]
                configuracion_juego.lista_nivel = lista_nivel
            else:
                numero = random.randint(0, (len(lista_con_juegos_dificiles) - 1))
                lista_nivel = lista_con_juegos_dificiles[numero]
                configuracion_juego.lista_nivel = lista_nivel

            for i in configuracion_juego.lista_nivel:
                fila = i[1]
                columna = i[2]
                restriccion = i[0]
                for j in self.lista_posicion_boton:
                    fila_boton = j[1]
                    columna_boton = j[2]
                    boton = j[0]
                    if fila == fila_boton and columna == columna_boton:
                        try:
                            restriccion = int(restriccion)
                        except:
                            pass
                        if isinstance(restriccion, int):
                            boton.config(text=restriccion)
                            boton["state"] = "disabled"
                            self.lista_botones_casilla[fila][columna] = (restriccion, columna)

            for i in lista_boton_donde_va_restriccion:
                for e in i:
                    try:
                        e.config(text="")
                    except:
                        pass

            for i in configuracion_juego.lista_nivel:
                fila = i[1]
                columna = i[2]
                restriccion = i[0]
                for j in lista_boton_donde_va_restriccion:
                    fila_comparar = j[0]
                    columna_comparar = j[1]
                    if fila == fila_comparar and columna == columna_comparar:
                        if restriccion == "<" or restriccion == ">":
                            j[2]["text"] = restriccion
                        elif len(j) == 3 and (restriccion == "v" or restriccion == "˄"):
                            j[2]["text"] = restriccion
                        elif len(j) == 4 and (restriccion == "v" or restriccion == "˄"):
                            j[3]["text"] = restriccion

            self.boton_1.config(state="disabled", bg="light blue")
            self.boton_2.config(state="disabled", bg="light blue")
            self.boton_3.config(state="disabled", bg="light blue")
            self.boton_4.config(state="disabled", bg="light blue")
            self.boton_5.config(state="disabled", bg="light blue")
            self.borrar_jugada["state"] = "disabled"
            self.terminar_juego["state"] = "disabled"
            self.borrar_juego["state"] = "disabled"
            self.iniciar_juego["state"] = "normal"
            self.guardar["state"] = "disabled"
            self.cargar["state"] = "normal"
            nombre.config(state="normal")
            nombre.delete(0, END)
            self.nombre_jugador = ""
            try:
                self.horas_reloj.after_cancel(contar_reloj)
            except:
                pass
            try:
                self.horas_reloj.after_cancel(contar_timer)
            except:
                pass

            if configuracion_juego.reloj == "Si":
                self.reloj("stop")
            elif configuracion_juego.reloj == "Timer":
                self.timer("stop", 0, 0, 0)

            lista_boton_numero_casilla = []

    # Metodo para borrar el juego
    def borrar_juego_funcion(self):
        global lista_boton_numero_casilla
        mensaje = messagebox.askyesno(title="", message="¿ESTÁ SEGURO DE BORRAR EL JUEGO (SI o NO)")
        if mensaje:
            while self.pila_jugadas != []:
                self.borrar_jugada_funcion()
            self.lista_botones_casilla = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]]

            self.boton_1.config(state="disabled", bg="light blue")
            self.boton_2.config(state="disabled", bg="light blue")
            self.boton_3.config(state="disabled", bg="light blue")
            self.boton_4.config(state="disabled", bg="light blue")
            self.boton_5.config(state="disabled", bg="light blue")
            self.borrar_jugada["state"] = "disabled"
            self.terminar_juego["state"] = "disabled"
            self.borrar_juego["state"] = "disabled"
            self.iniciar_juego["state"] = "normal"
            self.guardar["state"] = "disabled"
            self.cargar["state"] = "normal"
            try:
                self.horas_reloj.after_cancel(contar_reloj)
            except:
                pass
            try:
                self.horas_reloj.after_cancel(contar_timer)
            except:
                pass
            if configuracion_juego.reloj == "Si":
                self.reloj("stop")
            elif configuracion_juego.reloj == "Timer":
                self.timer("stop", 0, 0, 0)

            lista_boton_numero_casilla = []

    def top_10_funcion(self):
        try:
            self.reloj("pause")
        except:
            pass
        try:
            self.timer("pause", self.hh, self.mm, self.ss)
        except:
            pass
        ventana_top_10 = Toplevel(ventana_jugar)
        ventana_top_10.geometry("400x500")

        Label(ventana_top_10, text="TOP 10", font=("Arial", "16")).pack(anchor=W)

        archivo = open("futoshiki2021top10", "rb")
        lista = pickle.load(archivo)
        lista_facil = lista[0]
        lista_intermedio = lista[1]
        lista_dificil = lista[2]

        Label(ventana_top_10, text="NIVEL FACIL:        JUGADOR        TIEMPO", font=("Arial", "14")).pack(anchor=W)
        for i in lista_facil:
            espacios = 40 - len(str(i[0]))
            espacios_tiempo = 28 - len(str(i[1]))
            Label(ventana_top_10, text=" " * espacios + str(i[0]) + " " * espacios_tiempo + str(i[1]),font=("Arial", "14")).pack(anchor=W)

        Label(ventana_top_10, text="NIVEL INTERMEDIO:        JUGADOR        TIEMPO", font=("Arial", "14")).pack(anchor=W)
        for i in lista_intermedio:
            espacios = 40 - len(str(i[0]))
            espacios_tiempo = 28 - len(str(i[1]))
            Label(ventana_top_10, text=" " * espacios + str(i[0]) + " " * espacios_tiempo + str(i[1]),font=("Arial", "14")).pack(anchor=W)

        Label(ventana_top_10, text="NIVEL DIFICIL:        JUGADOR        TIEMPO", font=("Arial", "14")).pack(anchor=W)
        for i in lista_dificil:
            espacios = 40 - len(str(i[0]))
            espacios_tiempo = 28 - len(str(i[1]))
            Label(ventana_top_10, text=" " * espacios + str(i[0]) + " " * espacios_tiempo + str(i[1]),font=("Arial", "14")).pack(anchor=W)


        if configuracion_juego.reloj == "Timer" and self.iniciar_juego["state"] == "disabled":
            ventana_top_10.protocol("WM_DELETE_WINDOW",
                                    lambda: [self.timer("start", self.hh, self.mm, self.ss), ventana_top_10.destroy()])
        elif configuracion_juego.reloj == "Si" and self.iniciar_juego["state"] == "disabled":
            ventana_top_10.protocol("WM_DELETE_WINDOW", lambda: [self.reloj("start"), ventana_top_10.destroy()])
        ventana_top_10.mainloop()

    # Metodo para guardar partida
    def guardar_partida_funcion(self):
        # Variables necesarias guardar para el juego
        lista_texto_boton = []
        lista_estado_boton = []
        for i in self.lista_posicion_boton:
            lista_texto_boton.append(i[0].cget("text"))
            lista_estado_boton.append((i[0].cget("state")))
        lista_texto_restricciones = []
        for i in lista_boton_donde_va_restriccion:
            for j in i:
                try:
                    lista_texto_restricciones.append(j.cget("text"))
                except:
                    pass
        lista_botones_casilla = self.lista_botones_casilla
        nombre = self.nombre_jugador

        texto_en_horas = self.horas_reloj.cget("text")
        texto_en_minutos = self.minutos_reloj.cget("text")
        texto_en_segundos = self.segundos_reloj.cget("text")

        pila_jugadas = self.pila_jugadas

        lista_con_variables_juego = [lista_texto_boton, lista_estado_boton, lista_texto_restricciones,
                                     lista_botones_casilla, nombre, texto_en_horas, texto_en_minutos, texto_en_segundos,
                                     self.hh, self.mm, self.ss, pila_jugadas, lista_boton_numero_casilla]

        # Variables necesarias para la configuracion
        posicion = configuracion_juego.posicion
        nivel = configuracion_juego.nivel
        lista_nivel = configuracion_juego.lista_nivel
        reloj = configuracion_juego.reloj
        lista_timer = configuracion_juego.lista_timer

        lista_variables_config = [posicion, nivel, lista_nivel, reloj, lista_timer]

        lista_con_todo = [lista_con_variables_juego, lista_variables_config]

        archivo = open("futoshiki2021juegoactual.dat", "wb")
        pickle.dump(lista_con_todo, archivo)
        archivo.close()

    # Metodo para cargar partida
    def cargar_partida_funcion(self):
        global lista_boton_numero_casilla
        archivo = open("futoshiki2021juegoactual.dat", "rb")
        lista_con_todo = pickle.load(archivo)
        lista_con_variables_juego = lista_con_todo[0]

        lista_texto_boton = lista_con_variables_juego[0]
        lista_estado_boton = lista_con_variables_juego[1]
        for n, i in enumerate(self.lista_posicion_boton):
            i[0].config(text=lista_texto_boton[n], state=lista_estado_boton[n])

        lista_texto_restricciones = lista_con_variables_juego[2]
        for i in lista_boton_donde_va_restriccion:
            for n, j in enumerate(i):
                try:
                    j[n].config(text=lista_texto_restricciones[n])
                except:
                    pass

        lista_botones_casilla = lista_con_variables_juego[3]
        self.lista_botones_casilla = lista_botones_casilla

        nombre_jugador = lista_con_variables_juego[4]
        self.nombre_jugador = nombre_jugador

        nombre.config(state="normal")
        nombre.insert(0, nombre_jugador)

        nombre.config(state="disabled")

        texto_en_horas = lista_con_variables_juego[5]
        texto_en_minutos = lista_con_variables_juego[6]
        texto_en_segundos = lista_con_variables_juego[7]

        self.horas_reloj.config(text=texto_en_horas)
        self.minutos_reloj.config(text=texto_en_minutos)
        self.segundos_reloj.config(text=texto_en_segundos)

        self.hh = lista_con_variables_juego[8]
        self.mm = lista_con_variables_juego[9]
        self.ss = lista_con_variables_juego[10]

        pila_jugadas = lista_con_variables_juego[11]
        self.pila_jugadas = pila_jugadas

        lista_boton_numero_casilla = lista_con_variables_juego[12]

        lista_variables_config = lista_con_todo[1]

        posicion = lista_variables_config[0]
        nivel = lista_variables_config[1]
        lista_nivel = lista_variables_config[2]
        reloj = lista_variables_config[3]
        lista_timer = lista_variables_config[4]

        configuracion_juego.posicion = posicion
        configuracion_juego.nivel = nivel
        configuracion_juego.lista_nivel = lista_nivel
        configuracion_juego.reloj = reloj
        configuracion_juego.lista_timer = lista_timer

        self.cargo = True

        archivo.close()

    # Metodo para cada boton con el digito
    def boton_funcion(self, boton_numero):
        global lista_boton_numero_casilla
        lista_boton_numero_casilla = []
        lista_boton_numero_casilla.append(boton_numero)

    # Metodo para poner la casilla con el problema en rojo y despues presionar tecla y continuar
    def indicar_restriccion(self, lista_posiciones):
        for i in lista_posiciones:
            fila = i[0]
            columna = i[1]
            for j in self.lista_posicion_boton:
                fila_boton = j[1]
                columna_boton = j[2]
                if fila == fila_boton and columna == columna_boton:
                    j[0].config(bg="red")
        ventana_jugar.bind("<Return>", self.normalidad)

    # Metodo para volver los botones a color normal
    def normalidad(self, *args):
        for i in self.lista_posicion_boton:
            i[0].config(bg="light gray")

    # Metodo para cada casilla donde ira el metodo
    def casilla_funcion(self, fila, columna):
        lista_boton_numero_casilla.append(fila)
        lista_boton_numero_casilla.append(columna)
        if len(lista_boton_numero_casilla) == 3:
            # Revisar si hay una restriccion en esa casilla
            restriccion_valida_en_misma_casilla = True
            restriccion_valida_casilla_a_la_izquierda = True
            restriccion_valida_casilla_arriba = True
            for i in configuracion_juego.lista_nivel:
                restriccion = i[0]
                fila = i[1]
                columna = i[2]
                if fila == lista_boton_numero_casilla[1] and columna == lista_boton_numero_casilla[2]:
                    if restriccion == ">":
                        elemento = self.lista_botones_casilla[fila][columna + 1][0]
                        if elemento != 0:
                            if lista_boton_numero_casilla[0] > elemento:
                                restriccion_valida_en_misma_casilla = True
                                break
                            else:
                                restriccion_valida_en_misma_casilla = False
                                messagebox.showwarning(title="",
                                                       message="JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                                self.indicar_restriccion([(fila, columna), (fila, columna + 1)])
                        else:
                            restriccion_valida_en_misma_casilla = True
                            break

                    elif restriccion == "<":
                        elemento = self.lista_botones_casilla[fila][columna + 1][0]
                        if elemento != 0:
                            if lista_boton_numero_casilla[0] < elemento:
                                restriccion_valida_en_misma_casilla = True
                                break
                            else:
                                restriccion_valida_en_misma_casilla = False
                                messagebox.showwarning(title="",
                                                       message="JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                                self.indicar_restriccion([(fila, columna), (fila, columna + 1)])
                        else:
                            restriccion_valida_en_misma_casilla = True
                            break

                    elif restriccion == "v":
                        elemento = self.lista_botones_casilla[fila + 1][columna][0]
                        if elemento != 0:
                            if lista_boton_numero_casilla[0] > elemento:
                                restriccion_valida_en_misma_casilla = True
                                break
                            else:
                                restriccion_valida_en_misma_casilla = False
                                messagebox.showwarning(title="",
                                                       message="JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                                self.indicar_restriccion([(fila, columna), (fila + 1, columna)])
                        else:
                            restriccion_valida_en_misma_casilla = True
                            break
                    elif restriccion == "ʌ":
                        elemento = self.lista_botones_casilla[fila + 1][columna][0]
                        if elemento != 0:
                            if lista_boton_numero_casilla[0] < elemento:
                                restriccion_valida_en_misma_casilla = True
                                break
                            else:
                                restriccion_valida_en_misma_casilla = False
                                messagebox.showwarning(title="",
                                                       message="JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                                self.indicar_restriccion([(fila, columna), (fila + 1, columna)])
                        else:
                            restriccion_valida_en_misma_casilla = True
                            break

                elif fila == lista_boton_numero_casilla[1] and columna == (lista_boton_numero_casilla[2] - 1):
                    if restriccion == ">":
                        elemento = self.lista_botones_casilla[fila][columna][0]
                        if elemento != 0:
                            if lista_boton_numero_casilla[0] < elemento:
                                restriccion_valida_casilla_a_la_izquierda = True
                                break
                            else:
                                restriccion_valida_casilla_a_la_izquierda = False
                                messagebox.showwarning(title="",
                                                       message="JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                                self.indicar_restriccion([(fila, columna + 1), (fila, columna)])
                        else:
                            restriccion_valida_casilla_a_la_izquierda = True
                            break

                    elif restriccion == "<":
                        elemento = self.lista_botones_casilla[fila][columna][0]
                        if elemento != 0:
                            if lista_boton_numero_casilla[0] > elemento:
                                restriccion_valida_casilla_a_la_izquierda = True
                                break
                            else:
                                restriccion_valida_casilla_a_la_izquierda = False
                                messagebox.showwarning(title="",
                                                       message="JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                                self.indicar_restriccion([(fila, columna + 1), (fila, columna)])
                        else:
                            restriccion_valida_casilla_a_la_izquierda = True
                            break

                elif fila == (lista_boton_numero_casilla[1] - 1) and columna == (lista_boton_numero_casilla[2]):
                    if restriccion == "v":
                        elemento = self.lista_botones_casilla[fila][columna][0]
                        if elemento != 0:
                            if lista_boton_numero_casilla[0] < elemento:
                                restriccion_valida_casilla_arriba = True
                                break
                            else:
                                restriccion_valida_casilla_arriba = False
                                messagebox.showwarning(title="",
                                                       message="JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                                self.indicar_restriccion([(fila + 1, columna), (fila, columna)])
                        else:
                            restriccion_valida_casilla_arriba = True
                            break
                    elif restriccion == "ʌ":
                        elemento = self.lista_botones_casilla[fila][columna][0]
                        if elemento != 0:
                            if lista_boton_numero_casilla[0] > elemento:
                                restriccion_valida_casilla_arriba = True
                                break
                            else:
                                restriccion_valida_casilla_arriba = False
                                messagebox.showwarning(title="",
                                                       message="JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                                self.indicar_restriccion([(fila + 1, columna), (fila, columna)])
                        else:
                            restriccion_valida_casilla_arriba = True
                            break

            if restriccion_valida_en_misma_casilla and restriccion_valida_casilla_a_la_izquierda and restriccion_valida_casilla_arriba:
                restriccion_no_se_repite = True
                cont = 0
                while cont < 5:
                    elemento = self.lista_botones_casilla[lista_boton_numero_casilla[1]][cont][0]
                    if elemento == lista_boton_numero_casilla[0]:
                        messagebox.showwarning(title="",
                                               message="JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA ")
                        self.indicar_restriccion([(lista_boton_numero_casilla[1], lista_boton_numero_casilla[2]),
                                                  (lista_boton_numero_casilla[1], cont)])
                        restriccion_no_se_repite = False

                    elemento = self.lista_botones_casilla[cont][lista_boton_numero_casilla[2]][0]
                    if elemento == lista_boton_numero_casilla[0]:
                        messagebox.showwarning(title="",
                                               message="JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA ")
                        self.indicar_restriccion([(lista_boton_numero_casilla[1], lista_boton_numero_casilla[2]),
                                                  (cont, lista_boton_numero_casilla[2])])
                        restriccion_no_se_repite = False
                    cont += 1

                if restriccion_no_se_repite:
                    for i in self.lista_posicion_boton:
                        boton = i[0]
                        fila = i[1]
                        columna = i[2]
                        if fila == lista_boton_numero_casilla[1] and columna == lista_boton_numero_casilla[2]:
                            boton.config(text=lista_boton_numero_casilla[0])
                            self.lista_botones_casilla[lista_boton_numero_casilla[1]][lista_boton_numero_casilla[2]] = (
                            lista_boton_numero_casilla[0], lista_boton_numero_casilla[2])
                            self.pila_jugadas.append(
                                (lista_boton_numero_casilla[0], fila, lista_boton_numero_casilla[2]))
                    del lista_boton_numero_casilla[2]
                    del lista_boton_numero_casilla[1]
                else:
                    del lista_boton_numero_casilla[2]
                    del lista_boton_numero_casilla[1]
            else:
                del lista_boton_numero_casilla[2]
                del lista_boton_numero_casilla[1]

            tablero_completo = True

            for i in self.lista_botones_casilla:
                for j in i:
                    numero = j[0]
                    if numero == 0:
                        tablero_completo = False
                        break
                if tablero_completo is False:
                    break
            if tablero_completo:
                for i in self.lista_posicion_boton:
                    i[0]["state"] = "disabled"
                try:
                    self.reloj("pause")
                except:
                    pass
                try:
                    self.timer("pause", 0, 0, 0)
                except:
                    pass
                # TOP 10#################################################################
                # Proceso para ver si hay que registarlo en top 10
                # Obtener tiempo que duro
                if configuracion_juego.reloj == "Si" or configuracion_juego.reloj == "Timer":
                    formato = "%H:%M:%S"
                    hora = datetime.datetime.strptime((str(self.hh) + ":" + str(self.mm) + ":" + str(self.ss)), formato)
                    nombre = self.nombre_jugador

                    if configuracion_juego.reloj == "Timer":
                        tiempo_comparar = datetime.datetime.strptime((str(configuracion_juego.lista_timer[0]) + ":" + str(configuracion_juego.lista_timer[1]) + ":" + str(configuracion_juego.lista_timer[2])), formato)
                        hora = tiempo_comparar - hora
                        hora = datetime.datetime.strptime(str(hora), formato)
                        hora = hora.time()

                    #Abrir archivo top 10
                    archivo = open("futoshiki2021top10", "rb")
                    lista = pickle.load(archivo)
                    #listas
                    lista_facil = lista[0]
                    lista_intermedio = lista[1]
                    lista_dificil = lista[2]
                    #Comparar
                    if configuracion_juego.nivel == "Facil":
                        tupla = nombre, hora
                        lista_facil.append(tupla)
                        lista_facil.sort(key= lambda x: x[1])
                        if len(lista_facil) > 10:
                            lista_facil.pop()

                    elif configuracion_juego.nivel == "Intermedio":
                        tupla = nombre, hora
                        lista_intermedio.append(tupla)
                        lista_intermedio.sort(key= lambda x: x[1])
                        if len(lista_intermedio) > 10:
                            lista_intermedio.pop()
                    else:
                        tupla = nombre, hora
                        lista_dificil.append(tupla)
                        lista_dificil.sort(key=lambda x: x[1])
                        if len(lista_dificil) > 10:
                            lista_dificil.pop()


                    archivo = open("futoshiki2021top10", "wb")
                    listas = [lista_facil, lista_intermedio, lista_dificil]
                    pickle.dump(listas, archivo)
                    archivo.close()
                ##################################################################################

                messagebox.showinfo(title="", message="¡EXCELENTE! JUEGO TERMINADO CON ÉXITO.")
                alerta = messagebox.askyesno(title="", message="¿DESEA INICIAR UN NUEVO JUEGO?")
                if alerta:
                    self.terminar_juego_funcion(0)
        else:
            messagebox.showwarning(title="", message="FALTA QUE SELECCIONE UN DÍGITO.")


# ----------------------------------------------------------------#
# FUNCIONES
# ----------------------------------------------------------------#

configuracion_juego = Configuracion()
juego_obj = Juego()


def configuracion():
    configuracion_juego.ventana(ventana_principal)


def juego():
    juego_obj.widgets(ventana_principal, configuracion_juego)


# -----------------------------------------------------------------#
# PROGRAMA PRINCIPAL
# -----------------------------------------------------------------#

ventana_principal = Tk()
ventana_principal.geometry("400x400")
ventana_principal.title("Futoshiki")

barra_menu = Menu(ventana_principal)
barra_menu.add_command(label="Configuracion", command=configuracion)
barra_menu.add_command(label="A Jugar", command=juego)
barra_menu.add_command(label="Ayuda")
barra_menu.add_command(label="Acerca de", command=lambda: messagebox.showinfo(title="",
                                                                              message="Futoshiki\n Creador del juego: Carlos Leiva\n Fecha de creacion: 29/6/2021\n Version: 1.0"))
barra_menu.add_command(label="Salir", command=lambda: ventana_principal.destroy())

imagen = PhotoImage(file="futoshiki-math-switch-hero.png")
Label(ventana_principal, image=imagen).pack()

ventana_principal.config(menu=barra_menu)

ventana_principal.mainloop()
