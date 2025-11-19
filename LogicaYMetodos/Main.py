from LogicaYMetodos.Arbol import ArbolGeneral


class Control:
    def __init__(self):
        self.arbol = ArbolGeneral()
        self.carpetaActual = self.arbol.raiz


# para que no se ejecute al ser importado, solo cunado otro lo ocupe
if __name__ == "__main__":
    obj = Control()
    obj.main()
