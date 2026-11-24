"""Lista enlazada de reservas del vuelo, en orden de llegada."""

from pasajero import Pasajero


class Nodo:
    """Guarda un pasajero y el enlace al siguiente nodo."""

    def __init__(self, data: Pasajero):
        self.data = data
        self.next = None


class ListaPasajeros:
    """La cabeza apunta al primer nodo y cantidad cuenta las reservas."""

    def __init__(self):
        self.head = None
        self.cantidad = 0

    def ingresar(self, pasajero):
        """Agrega la nueva reserva al final de la lista."""
        nuevo = Nodo(pasajero)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo

        self.cantidad += 1
        return True

    def esta_vacia(self):
        return self.head is None

    def longitud(self):
        return self.cantidad

    def listar(self):
        """Recoge los pasajeros en el mismo orden en que reservaron."""
        resultado = []
        actual = self.head
        while actual is not None:
            resultado.append(actual.data)
            actual = actual.next
        return resultado

    def buscar(self, numero):
        """Busca un pasajero por su número de reserva."""
        actual = self.head
        while actual is not None:
            if actual.data.numero == numero:
                return actual.data
            actual = actual.next
        return None

    def buscar_por_asiento(self, asiento):
        """Busca al ocupante de un asiento."""
        actual = self.head
        while actual is not None:
            if actual.data.asiento == asiento:
                return actual.data
            actual = actual.next
        return None

    def buscar_por_cedula(self, cedula):
        """Compara las cédulas como texto para conservar los ceros iniciales."""
        actual = self.head
        while actual is not None:
            if actual.data.cedula == cedula:
                return actual.data
            actual = actual.next
        return None

    def modificar(self, numero, nuevo_nombre, nueva_edad, nuevo_asiento):
        """Actualiza los datos del pasajero en su posición original."""
        pasajero = self.buscar(numero)
        if pasajero is None:
            return False

        pasajero.nombre = nuevo_nombre
        pasajero.edad = nueva_edad
        pasajero.asiento = nuevo_asiento
        return True

    def eliminar(self, numero):
        """Desenlaza la reserva y devuelve el pasajero que salió."""
        anterior = None
        actual = self.head
        while actual is not None:
            if actual.data.numero == numero:
                if anterior is None:
                    self.head = actual.next       # Sale el primero.
                else:
                    anterior.next = actual.next   # El anterior enlaza al siguiente.
                self.cantidad -= 1
                return actual.data
            anterior = actual
            actual = actual.next
        return None

    def filtrar_por_clase(self, clase):
        """Recoge los pasajeros de la clase solicitada en orden de llegada."""
        resultado = []
        actual = self.head
        while actual is not None:
            if actual.data.clase() == clase:
                resultado.append(actual.data)
            actual = actual.next
        return resultado
