class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = [] if hijos is None else hijos
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)

# Metodos Getters y Setters
    def set_hijos(self, hijos):
        # Si hijos es None o no es un iterable (lista o tupla), inicializamos como lista vacía
        if hijos is None or not isinstance(hijos, (list, tuple)):
            self.hijos = []
        else:
            self.hijos = hijos
        for h in self.hijos:
            h.padre = self

    def get_hijos(self):
        return self.hijos

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_coste(self, coste):
        self.coste = coste

    def get_coste(self):
        return self.coste

    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista

    def __str__(self):
        return str(self.get_datos())