import tkinter as tk


# recibe como argumento un objeto de tipo Control y un metodo
def abrir_ventana_contraseñas(ArbolDeCarpetasContraseñas, actualizarPantalla):
    ventana_secundaria = tk.Toplevel()
    ancho = ventana_secundaria.winfo_screenwidth()  # obtiene el ancho de la pantalla
    alto = ventana_secundaria.winfo_screenheight()  # obtiene la altura de la pantalla
    ancho_ventana = 600
    alto_ventana = 800

    # metodo para guardar datos registrados
    def guardarContraseña():
        nombreObtenido = entrada1.get()
        usuarioObtenido = entrada2.get()
        contraseñaObtenido = entrada3.get()

        ArbolDeCarpetasContraseñas.arbol.agregarContraseña(
            nombreObtenido, usuarioObtenido, contraseñaObtenido
        )
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
    label = tk.Label(marco, text="Nueva contraseña", bg="Red", font=("Arial", 20))

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
        text="Nombre de la pagina web o aplicación:",
        anchor="w",
        font=("Arial", 15),
    )
    etiqueta1.pack(fill="x", padx=5, pady=2, side="top")
    entrada1 = tk.Entry(bloque1, relief="solid", font=("Arial", 14))
    entrada1.pack(fill="both", padx=5, pady=(0, 5), expand=True)

    bloque2 = tk.Frame(marco_Datos, width=550, height=80)
    bloque2.pack_propagate(False)
    bloque2.pack(pady=(60, 5))

    # Texto y campo de texto
    etiqueta2 = tk.Label(bloque2, text="Usuario:", anchor="w", font=("Arial", 15))
    etiqueta2.pack(fill="x", padx=5, pady=2, side="top")
    entrada2 = tk.Entry(bloque2, relief="solid")
    entrada2.pack(fill="both", padx=5, pady=(0, 5), expand=True)

    bloque3 = tk.Frame(marco_Datos, width=550, height=80)
    bloque3.pack_propagate(False)
    bloque3.pack(pady=(60, 0))

    # Texto y campo de texto
    etiqueta3 = tk.Label(bloque3, text="Contraseña:", anchor="w", font=("Arial", 15))
    etiqueta3.pack(fill="x", padx=5, pady=2, side="top")
    entrada3 = tk.Entry(bloque3, relief="solid")
    entrada3.pack(fill="both", padx=5, pady=(0, 5), expand=True)

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
    boton_continuar = tk.Button(
        marco_botones, text="Continuar", command=guardarContraseña
    )
    boton_salir.pack(side="left", padx=(50, 10), ipadx=20, fill="y")
    boton_continuar.pack(side="right", padx=(10, 50), ipadx=20, fill="y")

    marco_botones.pack_propagate(False)
    marco_botones.pack(fill="both", pady=100)

    ventana_secundaria.resizable(False, False)  # opion para que wayland no reescale
