# type: ignore

class Cliente:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None


class ColaClientes:
    def __init__(self):
        self.frente = None
        self.final = None

   
    def encolar(self, numero):
        nuevo = Cliente(numero)

        if self.frente is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

   
    def desencolar(self):
        if self.frente is None:
            print("La cola está vacía.")
            return None

        cliente = self.frente
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        return cliente.numero

    
    def peek(self):
        if self.frente is None:
            print("La cola está vacía.")
            return None

        return self.frente.numero

    
    def mostrar(self):
        actual = self.frente

        while actual is not None:
            print(actual.numero, end=" -> ")
            actual = actual.siguiente

        print("None")



cola = ColaClientes()


cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)

print("Contenido de la cola:")
cola.mostrar()


print("Próximo cliente a ser atendido:", cola.peek())
cliente_atendido = cola.desencolar()
print("Cliente atendido:", cliente_atendido)


print("Contenido de la cola después de desencolar:")
cola.mostrar()
