class PersonajeMCU:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas


def posicion_rocket_y_groot(pila):
    posicion = 0
    for i, personaje in enumerate(pila, start=1):
        if personaje.nombre == "Rocket Raccoon" or personaje.nombre == "Groot":
            posicion = i
            break
    return posicion


def personajes_mas_de_5_peliculas(pila):
    personajes = []
    for personaje in pila:
        if personaje.peliculas > 5:
            personajes.append((personaje.nombre, personaje.peliculas))
    return personajes


def participacion_viuda_negra(pila):
    total_peliculas = 0
    for personaje in pila:
        if personaje.nombre == "Black Widow":
            total_peliculas = personaje.peliculas
            break
    return total_peliculas


def personajes_con_iniciales(pila, iniciales):
    personajes = []
    for personaje in pila:
        if personaje.nombre[0] in iniciales:
            personajes.append(personaje.nombre)
    return personajes


# Ejemplo de uso
personajes_mcu = [
    PersonajeMCU("Iron Man", 4),
    PersonajeMCU("Captain America", 6),
    PersonajeMCU("Thor", 5),
    PersonajeMCU("Hulk", 3),
    PersonajeMCU("Black Widow", 8),
    PersonajeMCU("Hawkeye", 4),
    PersonajeMCU("Rocket Raccoon", 3),
    PersonajeMCU("Groot", 4),
]

posicion_rocket_groot = posicion_rocket_y_groot(personajes_mcu)
print("Posición de Rocket Raccoon y Groot:", posicion_rocket_groot)

personajes_mas_5_peliculas = personajes_mas_de_5_peliculas(personajes_mcu)
print("Personajes con más de 5 películas y su cantidad de participaciones:")
for personaje, peliculas in personajes_mas_5_peliculas:
    print(personaje, "- Películas:", peliculas)

participacion_viuda_negra = participacion_viuda_negra(personajes_mcu)
print("Participación de Black Widow:", participacion_viuda_negra, "películas")

personajes_iniciales = personajes_con_iniciales(personajes_mcu, "CDG")
print("Personajes cuyos nombres empiezan con C, D y G:")
for personaje in personajes_iniciales:
    print(personaje)

