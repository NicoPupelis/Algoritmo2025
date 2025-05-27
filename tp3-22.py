class PersonajeMCU:
    def __init__(self, nombre_personaje, superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.superheroe = superheroe
        self.genero = genero

    def __str__(self):
        return f"{self.nombre_personaje}, {self.superheroe}, {self.genero}"

def obtener_personaje_capitana_marvel(cola):
    for p in cola:
        if p.superheroe == "Capitana Marvel":
            print(p.nombre_personaje)
            break

def mostrar_superheroes_femeninos(cola):
    for p in cola:
        if p.genero == "F":
            print(p.superheroe)

def mostrar_personajes_masculinos(cola):
    for p in cola:
        if p.genero == "M":
            print(p.nombre_personaje)

def obtener_superheroe_scott_lang(cola):
    for p in cola:
        if p.nombre_personaje == "Scott Lang":
            print(p.superheroe)
            break

def mostrar_nombres_con_s(cola):
    for p in cola:
        if p.nombre_personaje.startswith("S") or p.superheroe.startswith("S"):
            print(p)

def buscar_carol_danvers(cola):
    for p in cola:
        if p.nombre_personaje == "Carol Danvers":
            print("Está en la cola como:", p.superheroe)
            return
    print("Carol Danvers no está en la cola.")

cola_mcu = [
    PersonajeMCU("Tony Stark", "Iron Man", "M"),
    PersonajeMCU("Steve Rogers", "Capitán América", "M"),
    PersonajeMCU("Natasha Romanoff", "Black Widow", "F"),
    PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"),
    PersonajeMCU("Scott Lang", "Ant-Man", "M"),
    PersonajeMCU("Stephen Strange", "Doctor Strange", "M"),
]

obtener_personaje_capitana_marvel(cola_mcu)
mostrar_superheroes_femeninos(cola_mcu)
mostrar_personajes_masculinos(cola_mcu)
obtener_superheroe_scott_lang(cola_mcu)
mostrar_nombres_con_s(cola_mcu)
buscar_carol_danvers(cola_mcu)
