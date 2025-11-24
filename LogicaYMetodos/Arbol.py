import json

import LogicaYMetodos.Nodos as Nodos


class ArbolGeneral:
    def __init__(self):
        self.raiz = Nodos.Carpeta("Raiz")  # carpeta es la clase y Nodos la libreria

    # si no se especifica a el padre, el padre sera la raiz
    def agregarCarpeta(self, nombreCarpetaAgregar, padre=None):
        if padre is None:
            padre = self.raiz
        carpetaAgregar = Nodos.Carpeta(nombreCarpetaAgregar, padre)
        carpetaAgregar.padre = padre  # Asegurar padre

        padre.hijos.append(carpetaAgregar)

    # si no se especifica a el padre, el padre sera la raiz
    def agregarContraseña(self, sitioWeb, usuario, contraseña, padre=None):
        if padre is None:
            padre = self.raiz
        nodo = Nodos.Contraseña(sitioWeb, usuario, contraseña, padre)
        padre.hijos.append(nodo)

    def mostrarHijos(self, carpetaRaiz=None):
        if carpetaRaiz == None:
            carpetaRaiz = self.raiz
        for (
            hijos
        ) in carpetaRaiz.hijos:  # muestra a los hijos de la carpeta raiz que se le pase
            # Para deferenciar cuales nodos son carpetas o contraseñas
            if isinstance(hijos, Nodos.Carpeta):
                print("Carpeta:", hijos.nombre)
            else:
                print("Contraseña:", hijos.nombre)  # hijos.nombre==hijos.sitioWeb
        return carpetaRaiz.hijos  # regresa los hijos

    def eliminarCarpeta(self, carpetaEliminar):
        while carpetaEliminar.hijos:
            carpetaEliminar.hijos.pop()
        padre = carpetaEliminar.padre
        if padre:  # comprueba que tiene padre o que sea distinto de None
            padre.hijos.remove(carpetaEliminar)

    def eliminarContraseña(self, contraseñaEliminar):
        padre = contraseñaEliminar.padre
        if padre:  # por seguridad, para no eliminar a el nodo raiz
            padre.hijos.remove(contraseñaEliminar)

    def buscarNodo(self, nombreNodo):
        def busquedaRecursiva(nodoActual):
            if nodoActual.nombre == nombreNodo:  # condicion de parada
                return nodoActual  # devuelve el nodo a la funcion que lo llamo
            for (
                hijos
            ) in nodoActual.hijos:  # condicion de parada cuando ya no hay mas hijos
                resultado = busquedaRecursiva(hijos)
                if resultado:
                    return resultado
            return None

        return busquedaRecursiva(self.raiz)

    # Metodo para guardar en un json
    def guardar(self, ruta="datos.json"):
        with open(ruta, "w") as f:
            json.dump(self.raiz.to_dict(), f, indent=4)

    # carga al inicio de la aplicacion
    def cargar(self, ruta="datos.json"):
        try:
            with open(ruta, "r") as f:
                data = json.load(f)
                self.raiz = self._construir_nodo(data, None)
        except FileNotFoundError:
            pass  # primera vez sin datos

    # Contruye la jerarquia
    def _construir_nodo(self, data, padre):
        if data["tipo"] == "carpeta":
            nodo = Nodos.Carpeta(data["nombre"], padre)
            nodo.hijos = [self._construir_nodo(h, nodo) for h in data["hijos"]]
            return nodo
        else:
            return Nodos.Contraseña(
                data["nombre"], data["usuario"], data["contraseña"], padre
            )
