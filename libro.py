from copia import Copia 
class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.copias = []

    def agregar_copia(self, idCopia: str, libro, ubicacion: str):
        nueva_copia = Copia(idCopia, libro, ubicacion)
        self.copias.append(nueva_copia)
        return nueva_copia

    def obtener_disponibles(self):
        disponibles = []
        for copia in self.copias:
            if copia.disponible:
                disponibles.append(copia)
        return disponibles