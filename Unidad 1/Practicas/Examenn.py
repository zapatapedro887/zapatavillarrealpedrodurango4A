
class Libro:
    def __init__(self, titulo, autor, año, codigo, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.codigo = codigo
        self.disponible = disponible

    def mostrar_info(self):
        print(f"Libro: {self.titulo} | Autor: {self.autor} | Año: {self.año} | Código: {self.codigo} | Disponible: {self.disponible}")

    def marcar_como_prestado(self):
        self.disponible = False

    def marcar_como_disponible(self):
        self.disponible = True


class Usuario:
    def __init__(self, nombre, id_usuario, correo):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo
        self.prestamos = []  

    def mostrar_info(self):
        print(f"Usuario: {self.nombre} | ID: {self.id_usuario} | Correo: {self.correo}")


class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.activo = False

    def registrar_prestamo(self):
        if not self.libro.disponible:
            print(f"No se puede registrar el préstamo: el libro '{self.libro.titulo}' no está disponible.")
            return False
        self.libro.marcar_como_prestado()
        self.activo = True
        print(f"Préstamo registrado: '{self.libro.titulo}' a {self.usuario.nombre} hasta {self.fecha_devolucion.strftime('%Y-%m-%d')}")
        return True


    def mostrar_info(self):
        estado = 'Activo' if self.activo else 'Finalizado'
        print(f"Préstamo -> Libro: {self.libro.titulo} | Usuario: {self.usuario.nombre} | Desde: {self.fecha_prestamo.strftime('%Y-%m-%d')} | Hasta: {self.fecha_devolucion.strftime('%Y-%m-%d')} | Estado: {estado}")


# ------------------ Simulación / demostración ------------------
if __name__ == '__main__':
    # Crear libros
    libro1 = Libro('Fundamentos de Programación', 'A. Autor', 2018, 'L001')
    libro2 = Libro('Algoritmos y Estructuras de Datos', 'B. Autor', 2020, 'L002')
    libro3 = Libro('Bases de Datos', 'C. Autor', 2016, 'L003')
    libro4 = Libro('Redes de Computadoras', 'D. Autor', 2019, 'L004')

    # Mostrar libros
    print('\n--- Libros ---')
    libro1.mostrar_info()
    libro2.mostrar_info()

    # Crear usuarios
    usuario1 = Usuario('Ana', 'U001', 'ana@uni.edu')
    estudiante1 = Estudiante('Carlos', 'E001', 'carlos@uni.edu', 'Ing. Sistemas', 6)
    estudiante2 = Estudiante('Luisa', 'E002', 'luisa@uni.edu', 'Ing. Informática', 4)
    profesor1 = Profesor('Dr. Martínez', 'P001', 'martinez@uni.edu', 'Ciencias de la Computación', 'Tiempo completo')
    profesor2 = Profesor('Dra. Gómez', 'P002', 'gomez@uni.edu', 'Ingeniería', 'Tiempo parcial')

    print('\n--- Usuarios (polimorfismo) ---')
    usuario1.mostrar_info()
    estudiante1.mostrar_info()
    profesor1.mostrar_info()

    # Simular préstamos
    print('\n--- Préstamos ---')
    prestamo1 = estudiante1.solicitar_prestamo(libro1, dias=7)  # estudiante pide libro1
    prestamo2 = profesor1.solicitar_prestamo(libro2, dias=21)  # profesor pide libro2

    # Mostrar estado de prestamos
    if prestamo1:
        prestamo1.mostrar_info()
    if prestamo2:
        prestamo2.mostrar_info()

    # Intentar prestar libro ya prestado
    print('\n--- Intento de préstamo sobre libro no disponible ---')
    estudiante2.solicitar_prestamo(libro1)

    # Devolver un libro
    print('\n--- Devoluciones ---')
    if prestamo1:
        prestamo1.devolver_libro()
        prestamo1.mostrar_info()

    # Verificar que el libro se marcó disponible
    print('\n--- Verificar disponibilidad ---')
    libro1.mostrar_info()

    # Mostrar lista de préstamos de un usuario
    print('\n--- Préstamos registrados para', estudiante1.nombre, '---')
    for p in estudiante1.prestamos:
        p.mostrar_info()

    print('\nSimulación finalizada.')
