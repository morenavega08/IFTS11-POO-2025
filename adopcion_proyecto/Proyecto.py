
class Perro:
    def __init__(self, id, nombre, raza, edad, tamaño, peso, salud, vacunado, temperamento):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.salud = salud
        self.vacunado = vacunado
        self.temperamento = temperamento
        self.estado = "disponible"

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_info(self):
        print(f"[{self.id}] {self.nombre}, {self.raza}, {self.edad} años, Estado: {self.estado}")


class UsuarioAdoptante:
    def __init__(self, nombre, dni, email, pref_raza, pref_edad, pref_tamaño):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = (pref_raza, pref_edad, pref_tamaño)
        self.historial = []

    def ver_historial(self):
        if not self.historial:
            print("Sin adopciones aún.")
        else:
            for perro in self.historial:
                print(f"Adoptado: {perro.nombre}")


class SistemaAdopcion:
    def __init__(self):
        self.perros = []
        self.usuarios = []

    def cargar_perro(self, perro):
        self.perros.append(perro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_disponibles(self):
        for perro in self.perros:
            if perro.estado == "disponible":
                perro.mostrar_info()

    def sugerir_perros(self, usuario):
        print("Sugerencias según tus preferencias:")
        for perro in self.perros:
            if (perro.raza == usuario.preferencias[0] or
                perro.edad <= usuario.preferencias[1] and
                perro.tamaño == usuario.preferencias[2]) and perro.estado == "disponible":
                perro.mostrar_info()

    def adoptar_perro(self, usuario, id_perro):
        for perro in self.perros:
            if perro.id == id_perro and perro.estado == "disponible":
                perro.cambiar_estado("adoptado")
                usuario.historial.append(perro)
                print(f"{usuario.nombre} adoptó a {perro.nombre}")
                return
        print("No se pudo realizar la adopción.")


sistema = SistemaAdopcion()

# Cargar para adoptar
sistema.cargar_perro(Perro(1, "Luna", "Shih Tzu", 19, "enana", 6.0, "Sana", True, "Vieja"))
sistema.cargar_perro(Perro(2, "Sasha", "Boxer", 9, "grande", 12.0, "Sana", True, "Juguetona"))
sistema.cargar_perro(Perro(3, "Puppy", "Caniche", 11, "mediana", 9.0, "Sana", True, "Protectora"))

# Registrar para adoptar
usuario = UsuarioAdoptante("Morena", "12345678", "Solecito@gmail.com", "Shih Tzu", 6, "enana")
sistema.registrar_usuario(usuario)

# Mostrar para adoptar
sistema.mostrar_disponibles()

# Sugerir
sistema.sugerir_perros(usuario)

# Adoptar un perro !!!
sistema.adoptar_perro(usuario, 1)

# Ver historial
usuario.ver_historial()
