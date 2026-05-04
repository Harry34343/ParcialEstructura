from Node import NodoCircular
class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

        actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        nuevo.next = self.head

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

    def JosephusModificado(self, m):
        current = self.head
        if current is None or current.next is None:
            return
        prev = None
        while current != current.next:
            for i in range(m-1):
                prev = current
                current = current.next
            prev.next = current.next
            print("Nodo eliminado: "+str(current.dato))
            if current.dato%5==0:
                current = current.next
                current = current.next
            current = current.next
        self.head = current
        return current
ll = ListaCircular()
ll.crear_lista(7)
ll.mostrar()
ll.JosephusModificado(3)
ll.mostrar()