class Nodo:  # clase padre que hereda atributos a carpeta y contraseña
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre
    
  

class Carpeta(Nodo):
    def __init__(self, nombre, padre=None):
        super().__init__(nombre, padre)
        self.hijos = []


class Contraseña(Nodo):
    def __init__(self, sitioWeb, usuario, contraseña, padre=None):
        super().__init__(sitioWeb, padre)
        self.usuario = usuario
        self.contraseña = contraseña
        self.hijos = []




    