class Cliente:
    def __init__(self, nombre, email, telefono):
        # Constructor de la clase Cliente que inicializa los atributos nombre, email y telefono
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        # Método especial que define cómo se debe representar el objeto Cliente como una cadena
        return f"Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"

class SistemaClientes:
    def __init__(self):
        # Constructor de la clase SistemaClientes que inicializa una lista vacía para almacenar clientes
        self.clientes = []

    def agregar_cliente(self, cliente):
        # Método para agregar un nuevo cliente al sistema
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' agregado al sistema.")

    def eliminar_cliente(self, nombre):
        # Método para eliminar un cliente por nombre
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                self.clientes.remove(cliente)
                print(f"Cliente '{nombre}' eliminado del sistema.")
                return
        print(f"No se encontró el cliente con el nombre '{nombre}'.")

    def buscar_cliente(self, nombre):
        # Método para buscar un cliente por nombre
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    def listar_clientes(self):
        # Método para listar todos los clientes
        if not self.clientes:
            print("No hay clientes registrados.")
        for cliente in self.clientes:
            print(cliente)


def main():
    sistema = SistemaClientes()  # Crear una instancia del sistema de gestión de clientes

    while True:
        # Imprimir el menú de opciones
        print("""
        Sistema de Gestión de Clientes
        ==============================
        1. Agregar un cliente
        2. Eliminar un cliente
        3. Buscar un cliente
        4. Listar todos los clientes
        5. Salir
        ==============================
        """)
        opcion = input("Seleccione una opción: ") # Leer la opción seleccionada por el usuario 

        if opcion == "1":
            # Opción para agregar un nuevo cliente
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Ingrese el email del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            cliente = Cliente(nombre, email, telefono) # Crear un nuevo objeto Cliente
            sistema.agregar_cliente(cliente) # Agregar el cliente al sistema
        elif opcion == "2":
           # Opción para eliminar un cliente existente 
            nombre = input("Ingrese el nombre del cliente a eliminar: ")
            sistema.eliminar_cliente(nombre)  # Eliminar el cliente del sistema
        elif opcion == "3":
            # Opción para buscar un cliente por nombre
            nombre = input("Ingrese el nombre del cliente a buscar: ")
            cliente = sistema.buscar_cliente(nombre)   # Buscar el cliente en el sistema
            if cliente:
                print(f"Cliente encontrado: {cliente}")  # Mostrar la información del cliente si se encuentra
            else:
                print(f"No se encontró el cliente con el nombre '{nombre}'.")  # Mostrar mensaje si no se encuentra
        elif opcion == "4":
            # Opción para listar todos los clientes
            sistema.listar_clientes()   # Listar todos los clientes en el sistema
        elif opcion == "5":
            # Opción para salir del sistema
            print("Saliendo del sistema de gestión de clientes.")
            break   # Salir del bucle while y terminar el programa
        else:
            # Manejar opción no válida
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main() # Ejecutar la función principal cuando se ejecuta el script
