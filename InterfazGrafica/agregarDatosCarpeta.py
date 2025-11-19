import tkinter as tk


# recibe como argumento un objeto de tipo Control y un metodo
def abrir_ventana_carpeta(ArbolDeCarpetasContraseñas, actualizarPantalla):
    ventana_secundaria = tk.Toplevel()
    ancho = ventana_secundaria.winfo_screenwidth()  # obtiene el ancho de la pantalla
    alto = ventana_secundaria.winfo_screenheight()  # obtiene la altura de la pantalla
    ancho_ventana = 600
    alto_ventana = 800

    # metodo para guardar carpeta
    def guardarCarpeta():
        nombreObtenido = entrada1.get()

        ArbolDeCarpetasContraseñas.arbol.agregarCarpeta(nombreObtenido)
        actualizarPantalla()
        ventana_secundaria.destroy()

    # calcular la posicion para centrar la ventana
    posicion_x = round(ancho / 2 - ancho_ventana / 2)
    posicion_y = round(alto / 2 - alto_ventana / 2)
    ventana_secundaria.geometry(
        f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}"
    )

    # barra de arriba para leyenda
    marco = tk.Frame(ventana_secundaria)
    marco.config(relief="solid", bg="#2596be", width=600, height=80)
    label = tk.Label(marco, text="Nueva carpeta", bg="Red", font=("Arial", 20))

    # expand permite expansion, fill ejecuta la expansion
    label.pack(expand=True, fill="both")
    marco.pack_propagate(False)
    marco.pack()

    # marco para agregar los datos
    marco_Datos = tk.Frame(ventana_secundaria)
    marco_Datos.config(relief="solid", bg="#d596be")

    # bloques para ingresar los datos
    bloque1 = tk.Frame(marco_Datos, width=550, height=80)
    bloque1.pack_propagate(False)
    bloque1.pack(pady=(60, 5))
    # Texto y campo de texto
    etiqueta1 = tk.Label(
        bloque1,
        text="Nombre de la carpeta",
        anchor="w",
        font=("Arial", 15),
    )
    etiqueta1.pack(fill="x", padx=5, pady=2, side="top")
    entrada1 = tk.Entry(bloque1, relief="solid", font=("Arial", 14))
    entrada1.pack(fill="both", padx=5, pady=(0, 5), expand=True)

    marco_Datos.pack_propagate(False)
    marco_Datos.pack(fill="both", expand=True)

    # marco para los botones de abajo
    marco_botones = tk.Frame(marco_Datos)
    marco_botones.config(relief="solid", bg="red", height=80)

    boton_salir = tk.Button(
        # solo destruye la ventana secundaria
        marco_botones,
        text="Cancelar",
        command=ventana_secundaria.destroy,
    )
    boton_continuar = tk.Button(marco_botones, text="Continuar", command=guardarCarpeta)
    boton_salir.pack(side="left", padx=(50, 10), ipadx=20, fill="y")
    boton_continuar.pack(side="right", padx=(10, 50), ipadx=20, fill="y")

    marco_botones.pack_propagate(False)
    marco_botones.pack(fill="both", pady=100)

    ventana_secundaria.resizable(False, False)  # opion para que wayland no reescale
