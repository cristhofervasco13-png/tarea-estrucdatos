
from pasajero import Pasajero


class MiLista:
    """Lista construida manualmente con un arreglo."""

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La lista está llena")
            return False

        if self.buscar(pasajero.numero) != -1:
            print("  El número de pasajero ya existe")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (lista vacía)")
            return

        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    # 3. Insertar en una posición
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > self.cantidad:
            return False

        if self.cantidad == self.capacidad:
            return False

        if self.buscar(pasajero.numero) != -1:
            return False

        i = self.cantidad

        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i = i - 1

        self.datos[posicion] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    # 4. Búsqueda lineal
    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i

        return -1

    # 5. Búsqueda binaria
    def buscar_binaria(self, numero):
        izquierda = 0
        derecha = self.cantidad - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2

            if self.datos[medio].numero == numero:
                return medio

            elif self.datos[medio].numero < numero:
                izquierda = medio + 1

            else:
                derecha = medio - 1

        return -1

    # 6. Modificar pasajero
    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento
        return True

    # 7. Eliminar por posición
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            return None

        pasajero = self.datos[posicion]

        i = posicion

        while i < self.cantidad - 1:
            self.datos[i] = self.datos[i + 1]
            i = i + 1

        self.cantidad = self.cantidad - 1
        self.datos[self.cantidad] = None

        return pasajero

    # 8. Eliminar por número
    def eliminar_por_valor(self, numero):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.eliminar_por_posicion(posicion)
        return True

    # 9. Ordenar ascendente
    def ordenar_asc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):

                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    # 10. Ordenar descendente
    def ordenar_desc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):

                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    # 11. Reversar lista
    def reversar(self):
        izquierda = 0
        derecha = self.cantidad - 1

        while izquierda < derecha:
            aux = self.datos[izquierda]
            self.datos[izquierda] = self.datos[derecha]
            self.datos[derecha] = aux

            izquierda = izquierda + 1
            derecha = derecha - 1

    # 12. Copiar lista
    def copiar(self):
        nueva_lista = MiLista(self.capacidad)

        for i in range(self.cantidad):
            nueva_lista.añadir(self.datos[i])

        return nueva_lista

    # 13. Longitud
    def longitud(self):
        return self.cantidad
