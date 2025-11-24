class Nodo:  # clase padre que hereda atributos a carpeta y contraseña
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre


class Carpeta(Nodo):
    def __init__(self, nombre, padre=None):
        super().__init__(nombre, padre)
        self.hijos = []

    # Para convertirlo en diccionario
    def to_dict(self):
        return {
            "tipo": "carpeta",
            "nombre": self.nombre,
            "hijos": [h.to_dict() for h in self.hijos],
        }


class Contraseña(Nodo):
    def __init__(self, sitioWeb, usuario, contraseña, padre=None):
        super().__init__(sitioWeb, padre)
        self.usuario = usuario
        self.contraseña = contraseña
        self.hijos = []

    # Para convertirlo en diccionario
    def to_dict(self):
        return {
            "tipo": "contraseña",
            "nombre": self.nombre,
            "usuario": self.usuario,
            "contraseña": self.contraseña,
        }
