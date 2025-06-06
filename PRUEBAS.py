class Perro:
    _contador_id = 1

    def __init__(self, nombre: str, raza: str, edad: int, tamaño: str, peso: float,
                 salud: str, vacunado: bool, temperamento: str):
        self.id = Perro._contador_id
        Perro._contador_id += 1

        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.salud = salud
        self.vacunado = vacunado
        self.temperamento = temperamento
        self.estado = "disponible"

    def cambiar_estado(self, nuevo_estado: str):
        self.estado = nuevo_estado

    def __str__(self):
        return f"[{self.id}] {self.nombre} | {self.raza}, {self.edad} años | Estado: {self.estado}"


class UsuarioAdoptante:
    def __init__(self, nombre: str, dni: str, email: str, pref_raza: str, pref_edad: int, pref_tamaño: str):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = (pref_raza, pref_edad, pref_tamaño)
        self.historial: List[Perro] = []

    def ver_historial(self):
        if not self.historial:
            print("🔸 No hay adopciones registradas.")
        else:
            print("📜 Historial de adopciones:")
            for perro in self.historial:
                print(f"- {perro.nombre} ({perro.raza})")


class SistemaAdopcion:
    def __init__(self):
        self.perros: List[Perro] = []
        self.usuarios: List[UsuarioAdoptante] = []

    def cargar_perro(self, perro: Perro):
        self.perros.append(perro)

    def registrar_usuario(self, usuario: UsuarioAdoptante):
        self.usuarios.append(usuario)

    def mostrar_disponibles(self):
        print("\n🐶 Perros disponibles:")
        disponibles = [p for p in self.perros if p.estado == "disponible"]
        if not disponibles:
            print("No hay perros disponibles.")
        for perro in disponibles:
            print(perro)

    def sugerir_perros(self, usuario: UsuarioAdoptante):
        print("\n🔍 Sugerencias para vos:")
        for perro in self.perros:
            if (
                perro.estado == "disponible"
                and perro.raza == usuario.preferencias[0]
                or (perro.edad <= usuario.preferencias[1] and perro.tamaño == usuario.preferencias[2])
            ):
                print(perro)

    def adoptar_perro(self, usuario: UsuarioAdoptante, id_perro: int):
        for perro in self.perros:
            if perro.id == id_perro:
                if perro.estado != "disponible":
                    print("❌ Ese perro ya no está disponible.")
                    return
                perro.cambiar_estado("adoptado")
                usuario.historial.append(perro)
                print(f"✅ ¡Felicidades! Adoptaste a {perro.nombre}.")
                return
        print("❌ ID de perro no encontrado.")


# ---------------- MENÚ INTERACTIVO ----------------

def menu():
    sistema = SistemaAdopcion()

    # Perros de prueba
    sistema.cargar_perro(Perro("Luna", "Labrador", 3, "grande", 25.0, "Sana", True, "Juguetona"))
    sistema.cargar_perro(Perro("Rocky", "Caniche", 2, "pequeño", 8.0, "Sana", True, "Tranquilo"))
    sistema.cargar_perro(Perro("Max", "Ovejero", 5, "grande", 30.0, "Sana", True, "Protector"))

    print("👤 Registrarse como usuario adoptante:")
    nombre = input("Nombre: ")
    dni = input("DNI: ")
    email = input("Email: ")
    pref_raza = input("Preferencia de raza: ")
    pref_edad = int(input("Edad máxima preferida: "))
    pref_tamaño = input("Tamaño preferido (pequeño/mediano/grande): ")

    usuario = UsuarioAdoptante(nombre, dni, email, pref_raza, pref_edad, pref_tamaño)
    sistema.registrar_usuario(usuario)

    while True:
        print("\n--- MENÚ ---")
        print("1. Ver perros disponibles")
        print("2. Ver sugerencias")
        print("3. Adoptar un perro")
        print("4. Ver historial de adopciones")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            sistema.mostrar_disponibles()
        elif opcion == "2":
            sistema.sugerir_perros(usuario)
        elif opcion == "3":
            try:
                id_perro = int(input("Ingresá el ID del perro que querés adoptar: "))
                sistema.adoptar_perro(usuario, id_perro)
            except ValueError:
                print("❌ Ingresá un número válido.")
        elif opcion == "4":
            usuario.ver_historial()
        elif opcion == "0":
            print("👋 Gracias por usar el sistema de adopción.")
            break
        else:
            print("❌ Opción no válida. Probá de nuevo.")


# Iniciar el sistema
if __name__ == "__main__":
    menu()
