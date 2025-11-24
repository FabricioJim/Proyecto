import tkinter as tk
from tkinter import messagebox
import subprocess
import os


BG = "#1e1e1e"         
FG = "#ffffff"         
BTN_BG = "#3c3c3c"     
BTN_HOVER = "#575757"  
ENTRY_BG = "#2a2a2a"   

def hover_in(btn):
    btn["bg"] = BTN_HOVER

def hover_out(btn):
    btn["bg"] = BTN_BG

def validar(win):

    usuario = win.entry_nombre.get().strip()
    contrasenia = win.entry_pass.get().strip()
    ruta = os.path.join(os.path.dirname(__file__),("login.txt"))
    with open(ruta,"r") as arch:
        valor1 = arch.readline().strip()
        valor2 = arch.readline().strip()
    
    print(valor1)
    print(valor2)

    if not contrasenia:
        messagebox.showerror("Error", "Escriba su contraseña")
        return
    if not usuario:
        messagebox.showerror("Error", "Escriba su nombre")
        return
    
    if usuario != valor1 or contrasenia != valor2:
        messagebox.showerror("Error","El usuario o contrasenia es incorrecto")
        return

    if usuario == valor1 and contrasenia == valor2:
        win.destroy()
        subprocess.run(["python", "-m", "InterfazGrafica.MenuPrincipal"])

def main():
    Principal = tk.Tk()
    Principal.title("Login")
    Principal.geometry("320x450")
    Principal.configure(bg=BG)
    Principal.resizable(False, False)


    titulo = tk.Label(
        Principal, text="Inicio de Sesión",
        fg=FG, bg=BG, font=("Helvetica", 18, "bold")
    )
    titulo.pack(pady=20)

    
    tk.Label(Principal, text="Usuario", fg=FG, bg=BG, font=("Helvetica", 12)).pack(pady=5)
    Principal.entry_nombre = tk.Entry(
        Principal, width=28, bg=ENTRY_BG, fg=FG, relief="flat",
        insertbackground=FG, font=("Helvetica", 11)
    )
    Principal.entry_nombre.pack(ipady=4)

    
    tk.Label(Principal, text="Contraseña", fg=FG, bg=BG, font=("Helvetica", 12)).pack(pady=15)
    Principal.entry_pass = tk.Entry(
        Principal, width=28, bg=ENTRY_BG, fg=FG, relief="flat",
        insertbackground=FG, font=("Helvetica", 11), show="*"
    )
    Principal.entry_pass.pack(ipady=4)


    btn = tk.Button(
        Principal, text="Confirmar", bg=BTN_BG, fg=FG,
        font=("Helvetica", 12, "bold"), relief="flat",
        command=lambda: validar(Principal)
    )
    btn.pack(pady=30, ipadx=20, ipady=8)

    # Hover
    btn.bind("<Enter>", lambda e: hover_in(btn))
    btn.bind("<Leave>", lambda e: hover_out(btn))

    Principal.mainloop()

main()