class usuario:
    def __init__(self, idUsuario: int, nombre: str, limite_prestamos,prestamos_activos: str):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.limite_prestamos=limite_prestamos
        self.prestamos_activos=prestamos_activos

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