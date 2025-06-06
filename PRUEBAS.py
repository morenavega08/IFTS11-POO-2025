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
        #  Estaría bueno validar que el nuevo_estado sea uno de los estados válidos
        # (por ejemplo, "disponible", "adoptado", "en_proceso").
        # Así evitás errores si se escribe algo mal.
        self.estado = nuevo_estado

    def __str__(self):
        return f"[{self.id}] {self.nombre} | {self.raza}, {self.edad} años | Estado: {self.estado}"


class UsuarioAdoptante:
    def __init__(self, nombre: str, dni: str, email: str, pref_raza: str, pref_edad: int, pref_tamaño: str):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        # Che ¿y si las preferencias son más flexibles? ejemplo, una lista de razas o un rango de edad.
        # Así el usuario no se limita tanto.
        self.preferencias = (pref_raza, pref_edad, pref_tamaño)
        self.historial: List[Perro] = []

    def ver_historial(self):
        if not self.historial:
            print("🔸 No hay adopciones registradas.")
        else:
            print("📜 Historial de adopciones:")
            for perro in self.historial:
                print(f"- {perro.nombre} ({perro.raza})")
