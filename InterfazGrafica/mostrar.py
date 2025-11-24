import tkinter as tk
import subprocess
from tkinter import messagebox
from LogicaYMetodos import Main, Nodos
from LogicaYMetodos.Arbol import ArbolGeneral

def mostrar_datos(text, a):

    win = text.get().strip()
    #busca el nombre del nodo en el objeto arbol 
    w = a.arbol.buscarNodo(win)
    #si w es none significa que no se encontro y retorna un mensaje de error
    if w is None:
        messagebox.showerror("Error","No se encontró el sitio")
        return
    
    ventana = tk.Toplevel()
    ventana.title("Datos")
    ventana.geometry("320x450")
    ventana.resizable(False, False)


    ventana.configure(bg="white")  

    titulo = tk.Label(
        ventana,
        text="Información del sitio",
        font=("Arial", 16, "bold"),
        bg="#f0f0f0"
    )
    titulo.pack(pady=10)
    #si si se encontro una coicidencia, muestra los datos optenidos de la siguiente forma
    label = tk.Label(
        ventana,
        text=f"Sitio: {w.nombre}\n\nUsuario: {w.usuario}\n\nContraseña: {w.contraseña}",
        font=("Arial", 13),
        bg="#ffffff",
        relief="solid",
        bd=1,
        padx=10,
        pady=10,
        justify="left"
    )

    label.pack(padx=20, pady=20, fill="both")

    ventana.mainloop()

