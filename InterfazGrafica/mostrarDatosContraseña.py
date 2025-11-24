import tkinter as tk
from tkinter import messagebox


def mostrarDatosDeLaContraseña(hijo, control, actualizarPantalla):
    ventana_secundaria = tk.Toplevel()
    ancho = ventana_secundaria.winfo_screenwidth()
    alto = ventana_secundaria.winfo_screenheight()

    ventana_secundaria.geometry(
        "600x800+{}+{}".format(round(ancho / 2 - 300), round(alto / 2 - 400))
    )

    # Barra superior
    marco = tk.Frame(ventana_secundaria, bg="#2596be", width=600, height=80)
    label = tk.Label(
        marco,
        text="Datos de la contraseña:",
        bg="#2596be",
        fg="white",
        font=("Arial", 20),
    )
    label.pack(expand=True, fill="both")
    marco.pack_propagate(False)
    marco.pack()

    # Marco principal
    marco_Datos = tk.Frame(ventana_secundaria, bg="#d596be")
    marco_Datos.pack(fill="both", expand=True)

    # ---------- BLOQUE NOMBRE ----------
    bloque_uno = tk.Frame(marco_Datos, width=550, height=80)
    bloque_uno.pack(pady=(60, 5))
    bloque_uno.pack_propagate(False)

    tk.Label(bloque_uno, text="Nombre del sitio:", anchor="w", font=("Arial", 15)).pack(
        fill="x", padx=5
    )

    tk.Label(bloque_uno, text=hijo.nombre, relief="solid", font=("Arial", 14)).pack(
        fill="both", padx=5, pady=(0, 5), expand=True
    )

    # ---------- BLOQUE USUARIO ----------
    bloque_dos = tk.Frame(marco_Datos, width=550, height=80)
    bloque_dos.pack(pady=(60, 5))
    bloque_dos.pack_propagate(False)

    tk.Label(bloque_dos, text="Usuario:", anchor="w", font=("Arial", 15)).pack(
        fill="x", padx=5
    )

    tk.Label(bloque_dos, text=hijo.usuario, relief="solid", font=("Arial", 14)).pack(
        fill="both", padx=5, pady=(0, 5), expand=True
    )

    # ---------- BLOQUE CONTRASEÑA ----------
    bloque_tres = tk.Frame(marco_Datos, width=550, height=80)
    bloque_tres.pack(pady=(60, 5))
    bloque_tres.pack_propagate(False)

    tk.Label(bloque_tres, text="Contraseña:", anchor="w", font=("Arial", 15)).pack(
        fill="x", padx=5
    )

    tk.Label(
        bloque_tres, text=hijo.contraseña, relief="solid", font=("Arial", 14)
    ).pack(fill="both", padx=5, pady=(0, 5), expand=True)

    # ---------- BOTONES INFERIORES ----------
    marco_botones = tk.Frame(marco_Datos, height=80)
    marco_botones.pack(fill="both", pady=60)
    marco_botones.pack_propagate(False)

    # Botón cancelar
    tk.Button(marco_botones, text="Cancelar", command=ventana_secundaria.destroy).pack(
        side="left", padx=40, ipadx=20
    )

    # Botón eliminar
    def eliminar():
        respuesta = messagebox.askyesno(
            "Confirmar eliminación", "¿Seguro que deseas eliminar esta contraseña?"
        )
        if respuesta:
            control.eliminarContraseña(hijo.nombre, control.carpetaActual)
            actualizarPantalla()  # Actualiza ventana principal
            ventana_secundaria.destroy()

    tk.Button(
        marco_botones, text="Eliminar", bg="#c65353", fg="white", command=eliminar
    ).pack(side="right", padx=40, ipadx=20)

    ventana_secundaria.resizable(False, False)
