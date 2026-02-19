from libro import Libro
class Copia:
    def __init__(self, id_copia: str, libro: Libro, ubicacion: str):
        self.id_copia = id_copia
        self.libro = libro
        self.ubicacion = ubicacion
        self.disponible = False

    def get_estado(self) -> str:
        if self.disponible:
            return "Disponible"
        else:
            return "Prestado"

    def prestar(self) -> bool:
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self) -> None:
        self.disponible = True