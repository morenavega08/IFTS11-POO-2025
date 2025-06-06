# Notas

def sugerir_perros(self, usuario):
        print("Sugerencias según tus preferencias:")
        for perro in self.perros:
            if (perro.raza == usuario.preferencias[0] or
                perro.edad <= usuario.preferencias[1] and
                perro.tamaño == usuario.preferencias[2]) and perro.estado == "disponible":
                perro.mostrar_info()

#otras notas
  if perro_encontrado is None:
                raise ValueError(f"No se encontró un perro reservado con ID {perro_id}.")
        for usuario in self.usuarios:
            if usuario.dni == usuario_dni:
                usuario_encontrado= usuario
                break

#Recomendaciones de la IA
def __str__(self):
    return f"[{self.id}] {self.nombre}, {self.raza}, {self.edad} años, Estado: {self.estado}"
print(perro)  # en vez de perro.mostrar_info()

class Perro:
    contador_id = 1

    def __init__(self, nombre, raza, edad, tamaño, peso, salud, vacunado, temperamento):
        self.id = Perro.contador_id
        Perro.contador_id += 1
        ...
while True:
    print("1. Ver perros disponibles")
    print("2. Sugerencias según preferencias")
    print("3. Adoptar")
    print("4. Ver historial")
    print("0. Salir")
    opcion = input("Elija una opción: ")
    ...
