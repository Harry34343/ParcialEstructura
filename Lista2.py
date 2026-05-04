from Node2 import NodoSimple
class ListaSimple:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoSimple(dato)

        if not self.head:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        print(" -> ".join(resultado) + " -> None")

    def partir_voltear_intercalar(self):
        current = self.head
        if current is None:
            return
        end = current
        while end.next:
            end = end.next
        temp = current
        while (current.next != end):
            temp = current
            while temp != end:
                temp = temp.next
            end = temp
            prev = current
            current = current.next
        MiddleNode = prev
        print("MiddleNode: "+str(MiddleNode.dato))
        Node = MiddleNode
        prevGroup = self.getPrev(Node)
        prev = None
        while Node:
            next = Node.next
            Node.next = prev
            prev = Node
            Node = next
        prevGroup.next = prev
        
        return
    
    def getPrev(self, head):
        temp = self.head
        while temp.next != head:
            temp = temp.next
        return temp
ll = ListaSimple()
ll.insertar_final(1)
ll.insertar_final(2)
ll.insertar_final(3)
ll.insertar_final(4)
ll.insertar_final(5)
ll.insertar_final(6)
ll.mostrar()
ll.partir_voltear_intercalar()
ll.mostrar()