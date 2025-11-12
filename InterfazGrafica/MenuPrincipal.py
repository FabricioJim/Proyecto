import tkinter as tk

ventana_principal = tk.Tk()
ancho = ventana_principal.winfo_screenwidth()  # obtiene el ancho de la pantalla
alto = ventana_principal.winfo_screenheight()  # obtiene la altura de la pantalla

ancho_ventana = 600
alto_ventana = 800

# calcular la posicion para centrar la ventana
posicion_x = round(ancho / 2 - ancho_ventana / 2)
posicion_y = round(alto / 2 - alto_ventana / 2)

ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
# barra de busqueda y botones
marco = tk.Frame(ventana_principal)
marco.config(relief="solid", bg="#2596be", width=600, height=80)
boton_ingresarCarpeta = tk.Button(marco, text="Ingresar Carpeta")
boton_ingresarContraseña = tk.Button(marco, text="Ingresar contraseña")
boton_ParaBuscar = tk.Button(marco, text="Buscar")

text = tk.Entry(marco, relief="solid")


# pad para el espacio entre widgets y ipad para el relleno de widgets
text.pack(side="left", ipady=8, padx=(10, 5))
boton_ParaBuscar.pack(side="left", padx=(5, 10), ipadx=10, ipady=8)
boton_ingresarContraseña.pack(side="right", padx=(10, 20), ipadx=0, ipady=8)
boton_ingresarCarpeta.pack(side="right", padx=(10, 20), ipady=8)
marco.pack_propagate(False)
marco.pack()

# marco para mostrar la informacion de carpetas y contraseñas
marco_Datos = tk.Frame(ventana_principal)
marco_Datos.config(relief="solid", bg="#d596be", width=600, height=720)

marco_Datos.pack()
ventana_principal.resizable(False, False)  # opion para que wayland no reescale
ventana_principal.mainloop()
