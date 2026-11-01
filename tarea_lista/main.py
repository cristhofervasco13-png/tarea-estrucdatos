
from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        if self.buscar(pasajero.numero) != -1:
            return False

        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print("  (lista vacía)")
            return

        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # 3. Insertar
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            return False

        if self.buscar(pasajero.numero) != -1:
            return False

        self.pasajeros.insert(posicion, pasajero)
        return True

    # 4. Buscar con comprensión
    def buscar(self, numero):
        posiciones = [
            i for i, p in enumerate(self.pasajeros)
            if p.numero == numero
        ]

        if posiciones:
            return posiciones[0]

        return -1

    # 5. Búsqueda binaria
    def buscar_binaria(self, numero):
        numeros = [p.numero for p in self.pasajeros]

        posicion = bisect_left(numeros, numero)

        if posicion < len(numeros) and numeros[posicion] == numero:
            return posicion

        return -1

    # 6. Modificar
    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.pasajeros[posicion].destino = nuevo_destino
        self.pasajeros[posicion].asiento = nuevo_asiento

        return True

    # 7. Eliminar por posición
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            return None

        return self.pasajeros.pop(posicion)

    # 8. Eliminar por número
    def eliminar_por_valor(self, numero):
        nueva_lista = [
            p for p in self.pasajeros
            if p.numero != numero
        ]

        if len(nueva_lista) == len(self.pasajeros):
            return False

        self.pasajeros = nueva_lista
        return True

    # 9. Ordenar ascendente
    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    # 10. Ordenar descendente
    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    # 11. Reversar
    def reversar(self):
        self.pasajeros.reverse()

    # 12. Copiar
    def copiar(self):
        nueva_lista = ListaPython()
        nueva_lista.pasajeros = self.pasajeros.copy()
        return nueva_lista

    # 13. Longitud
    def longitud(self):
        return len(self.pasajeros)

    # 14. Filtrar por destino
    def filtrar_por_destino(self, destino):
        return [
            p for p in self.pasajeros
            if p.destino.lower() == destino.lower()
        ]

    # 15. Mayores de edad
    def mayores_de_edad(self):
        return [
            p for p in self.pasajeros
            if p.es_mayor_de_edad()
        ]
