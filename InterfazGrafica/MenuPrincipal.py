import tkinter as tk

from LogicaYMetodos import Main, Nodos

ventana_principal = tk.Tk()
ancho = ventana_principal.winfo_screenwidth()  # obtiene el ancho de la pantalla
alto = ventana_principal.winfo_screenheight()  # obtiene la altura de la pantalla

icono_carpeta = tk.PhotoImage(file="InterfazGrafica/LogoCarpeta.png")
icono_contraseña = tk.PhotoImage(file="InterfazGrafica/LogoContraseña.png")
icono_agregarContraseña = tk.PhotoImage(file="InterfazGrafica/agregarContraseña.png")
icono_agregarCarpeta = tk.PhotoImage(file="InterfazGrafica/agregarCarpeta.png")
icono_buscar = tk.PhotoImage(file="InterfazGrafica/buscar.png")
icono_salir = tk.PhotoImage(file="InterfazGrafica/salida.png")


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
    # abre el archuvo agregarDatosContraseña
    command=abrirVentanaSecundariaContraseñas,
)
boton_salir = tk.Button(marco, image=icono_salir, compound="center")
boton_ParaBuscar = tk.Button(marco, image=icono_buscar, compound="center")

text = tk.Entry(marco, relief="solid")


# pad para el espacio entre widgets y ipad para el relleno de widgets
text.pack(side="left", ipady=8, padx=(25, 25))
boton_ParaBuscar.pack(side="left", padx=(5, 10), ipadx=10, ipady=8)
boton_salir.pack(side="left", padx=(35, 25), ipadx=10, ipady=8)
boton_ingresarContraseña.pack(side="right", padx=(10, 25), ipadx=10, ipady=8)
boton_ingresarCarpeta.pack(side="right", padx=(10, 35), ipady=8, ipadx=10)
marco.pack_propagate(False)
marco.pack()

# marco para mostrar la informacion de carpetas y contraseñas
marco_Datos = tk.Frame(ventana_principal)
marco_Datos.config(relief="solid", bg="#d596be", width=600, height=720)


# bloques para contraseñas y carpetas
def crearBloques(hijo):
    bloque = tk.Frame(marco_Datos, width=550, height=80)
    if isinstance(hijo, Nodos.Carpeta):
        icono = icono_carpeta
    else:
        icono = icono_contraseña

    boton = tk.Button(bloque, text=hijo.nombre, image=icono, compound="left")
    boton.image = icono
    # expand permite expansion, fill ejecuta la expansion
    boton.pack(expand=True, fill="both")
    bloque.pack_propagate(False)

    return bloque


# metodo para mostrar carpetas y contraseñas
def mostrarCarpetasContraseñas(control):
    # control.arbol ya es el arbol general y accede a su metodo mostrar hijos
    hijos = control.arbol.mostrarHijos()
    for hijo in hijos:
        Boton1 = crearBloques(hijo)
        Boton1.pack(pady=(10, 5))


# objeto de tipo control
ArbolDeCarpetasContraseñas = Main.Control()
# ArbolDeCarpetasContraseñas.main()
mostrarCarpetasContraseñas(ArbolDeCarpetasContraseñas)


# metodo para actualizar la ventana con nuevas contraseñas o carpetas
def actualizarPantalla():
    # recorre cada objeto que hay en marco_datos y despues los elimina
    for bloques in marco_Datos.winfo_children():
        bloques.destroy()
    # muestra lo nuevo
    mostrarCarpetasContraseñas(ArbolDeCarpetasContraseñas)


marco_Datos.pack_propagate(False)
marco_Datos.pack()
ventana_principal.resizable(False, False)  # opion para que wayland no reescale
ventana_principal.mainloop()
