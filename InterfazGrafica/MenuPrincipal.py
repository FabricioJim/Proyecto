import tkinter as tk

from LogicaYMetodos import Main, Nodos

from .mostrar import mostrar_datos

ventana_principal = tk.Tk()
ancho = ventana_principal.winfo_screenwidth()  # obtiene el ancho de la pantalla
alto = ventana_principal.winfo_screenheight()  # obtiene la altura de la pantalla

icono_carpeta = tk.PhotoImage(file="InterfazGrafica/LogoCarpeta.png")
icono_contraseña = tk.PhotoImage(file="InterfazGrafica/LogoContraseña.png")
icono_agregarContraseña = tk.PhotoImage(file="InterfazGrafica/agregarContraseña.png")
icono_agregarCarpeta = tk.PhotoImage(file="InterfazGrafica/agregarCarpeta.png")
icono_buscar = tk.PhotoImage(file="InterfazGrafica/buscar.png")
icono_salir = tk.PhotoImage(file="InterfazGrafica/salida.png")

# boton para eliminar carpeta
menu_contextual = tk.Menu(ventana_principal, tearoff=0)


ancho_ventana = 600
alto_ventana = 800

# calcular la posicion para centrar la ventana
posicion_x = round(ancho / 2 - ancho_ventana / 2)
posicion_y = round(alto / 2 - alto_ventana / 2)

ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
# barra de busqueda y botones
marco = tk.Frame(ventana_principal)
marco.config(relief="solid", bg="#2596be", width=600, height=80)


# abre una ventana secundaria para agregar contraseñas
def abrirVentanaSecundariaContraseñas():
    import InterfazGrafica.agregarDatosContraseña as ventana

    ventana.abrir_ventana_contraseñas(ArbolDeCarpetasContraseñas, actualizarPantalla)


# metodo para abrir una ventana secundaria para agregar carpetas
def abrirVentanaSecundariaCarpeta():
    import InterfazGrafica.agregarDatosCarpeta as ventana

    ventana.abrir_ventana_carpeta(ArbolDeCarpetasContraseñas, actualizarPantalla)


def abrirVentanaMostrarContraseña(hijo):
    import InterfazGrafica.mostrarDatosContraseña as ventana

    ventana.mostrarDatosDeLaContraseña(
        hijo, ArbolDeCarpetasContraseñas, actualizarPantalla
    )


boton_ingresarCarpeta = tk.Button(
    marco,
    image=icono_agregarCarpeta,
    compound="center",
    command=abrirVentanaSecundariaCarpeta,
)

boton_ingresarContraseña = tk.Button(
    marco,
    image=icono_agregarContraseña,
    compound="center",
    # abre el archivo agregarDatosContraseña
    command=abrirVentanaSecundariaContraseñas,
)
boton_salir = tk.Button(
    marco, image=icono_salir, compound="center", command=ventana_principal.destroy
)
boton_ParaBuscar = tk.Button(marco, image=icono_buscar, compound="center")

text = tk.Entry(marco, relief="solid")
# objeto de tipo control
# hasta aca para evitarnos de broncas
ArbolDeCarpetasContraseñas = Main.Control()
ArbolDeCarpetasContraseñas.arbol.cargar()

ArbolDeCarpetasContraseñas.carpetaActual = ArbolDeCarpetasContraseñas.arbol.raiz


# pad para el espacio entre widgets y ipad para el relleno de widgets
text.pack(side="left", ipady=8, padx=(25, 25))
# de este lado para evitarnos de broncas, asi le pasamos el texto y el arbol donde se estan aguardando las contrasenias
boton_ParaBuscar = tk.Button(
    marco,
    image=icono_buscar,
    compound="center",
    command=lambda: mostrar_datos(text, ArbolDeCarpetasContraseñas),
)

boton_ParaBuscar.pack(side="left", padx=(5, 10), ipadx=10, ipady=8)
boton_salir.pack(side="left", padx=(35, 25), ipadx=10, ipady=8)
boton_ingresarContraseña.pack(side="right", padx=(10, 25), ipadx=10, ipady=8)
boton_ingresarCarpeta.pack(side="right", padx=(10, 35), ipady=8, ipadx=10)
marco.pack_propagate(False)

# --- Marco del botón Regresar ---
marco_regresar = tk.Frame(ventana_principal, width=600, height=80, bg="#d596be")
marco_regresar.pack_propagate(False)


def botonRegresar():
    ArbolDeCarpetasContraseñas.regresarCarpeta()
    actualizarPantalla()


# botón REGRESAR con tamaño de bloque (80px)
boton_regresar = tk.Button(
    marco_regresar, text="⮌ Regresar", font=("Arial", 14), command=botonRegresar
)
boton_regresar.pack(expand=True, fill="both")


# marco para mostrar la informacion de carpetas y contraseñas
marco_Datos = tk.Frame(ventana_principal)
marco_Datos.config(relief="solid", bg="purple", width=600, height=720)


def eliminarCarpetaDesdeUI(carpeta):
    ArbolDeCarpetasContraseñas.eliminarCarpeta(carpeta.nombre)
    actualizarPantalla()


# bloques para contraseñas y carpetas
def crearBloques(hijo):
    bloque = tk.Frame(marco_Datos, width=550, height=80)
    if isinstance(hijo, Nodos.Carpeta):
        icono = icono_carpeta

        # Metodo para mostrar la carpeta seleccionada
        def accion():
            # cambiar carpeta actual
            ArbolDeCarpetasContraseñas.cambiarCarpetaActual(hijo)
            actualizarPantalla()

    else:
        icono = icono_contraseña

        def accion():
            abrirVentanaMostrarContraseña(hijo)

    boton = tk.Button(
        bloque, text=hijo.nombre, image=icono, compound="left", command=accion
    )
    boton.image = icono
    # expand permite expansion, fill ejecuta la expansion
    boton.pack(expand=True, fill="both")
    bloque.pack_propagate(False)

    # --------- MENÚ CONTEXTUAL SOLO PARA CARPETAS ----------
    if isinstance(hijo, Nodos.Carpeta):
        menu_carpeta = tk.Menu(ventana_principal, tearoff=0)
        menu_carpeta.add_command(
            label="Eliminar carpeta",
            command=lambda: (
                ArbolDeCarpetasContraseñas.eliminarCarpeta(hijo.nombre),
                actualizarPantalla(),
            ),
        )

        # Mostrar menú con clic derecho
        def mostrar_menu(event):
            menu_carpeta.tk_popup(event.x_root, event.y_root)

        boton.bind("<Button-3>", mostrar_menu)
    # -------------------------------------------------------
    return bloque


# metodo para mostrar carpetas y contraseñas
def mostrarCarpetasContraseñas(control):
    # se manda a llamar al metodo de la clase control
    hijos = control.obtenerHijos()
    for hijo in hijos:
        Boton1 = crearBloques(hijo)
        Boton1.pack(pady=(10, 5))


# metodo para actualizar la ventana con nuevas contraseñas o carpetas
def actualizarPantalla():
    # --- Mostrar u ocultar el botón regresar ----
    if ArbolDeCarpetasContraseñas.carpetaActual.padre is None:
        marco_regresar.forget()  # Ocultar en la raíz
    else:
        marco_regresar.pack(before=marco_Datos, fill="x")  # Mostrar cuando NO es raíz

    for bloques in marco_Datos.winfo_children():
        bloques.destroy()

    # muestra lo nuevo
    mostrarCarpetasContraseñas(ArbolDeCarpetasContraseñas)


marco.pack()
marco_regresar.pack()  # botón regresar (luego se ocultará si es raíz)
marco_Datos.pack_propagate(False)
marco_Datos.pack()


actualizarPantalla()


ventana_principal.resizable(False, False)  # opion para que wayland no reescale
ventana_principal.mainloop()
