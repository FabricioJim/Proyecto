from LogicaYMetodos.Arbol import ArbolGeneral, Nodos


class Control:
    def __init__(self):
        self.arbol = ArbolGeneral()
        self.carpetaActual = self.arbol.raiz

    # Manejo de carpetas y contraseñas
    def agregarCarpeta(self, nombre):
        self.arbol.agregarCarpeta(nombre, padre=self.carpetaActual)

    def agregarContraseña(self, sitio, usuario, contraseña):
        self.arbol.agregarContraseña(
            sitio, usuario, contraseña, padre=self.carpetaActual
        )

    # --- Navegación ---
    def cambiarCarpetaActual(self, carpeta):
        self.carpetaActual = carpeta

    # --- Lecturas ---
    def obtenerHijos(self):
        return self.carpetaActual.hijos

    def buscar(self, nombre):
        return self.arbol.buscarNodo(nombre)

    # --- Eliminar ---
    def eliminarCarpeta(self, nombre):
        nodo = self.buscar(nombre)
        if isinstance(nodo, Nodos.Carpeta):
            self.arbol.eliminarCarpeta(nodo)

    def eliminarContraseña(self, nombre, padre):
        # padre es la carpeta actual
        for hijo in padre.hijos:
            if isinstance(hijo, Nodos.Contraseña) and hijo.nombre == nombre:
                padre.hijos.remove(hijo)
                return True
        return False

    # ---Regresar a la carpeta anterior-----
    def regresarCarpeta(self):
        if self.carpetaActual.padre is not None:
            self.carpetaActual = self.carpetaActual.padre


if __name__ == "__main__":
    c = Control()
