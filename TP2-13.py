
pila_trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Impecable"},
    {"modelo": "Mark V", "pelicula": "Iron Man 2", "estado": "Destruido"},
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Impecable"},
    {"modelo": "Mark XLIV", "pelicula": "Iron Man 3", "estado": "Dañado"},
]

peliculas_hulkbuster = []
for traje in pila_trajes:
    if traje["modelo"] == "Mark XLIV":
        peliculas_hulkbuster.append(traje["pelicula"])

if peliculas_hulkbuster:
    print("El modelo Mark XLIV fue usado en las siguientes películas:")
    for pelicula in peliculas_hulkbuster:
        print("-", pelicula)
else:
    print("El modelo Mark XLIV no fue usado.")

modelos_danados = []
pila_aux = []

while pila_trajes:
    traje = pila_trajes.pop()
    if traje["estado"] == "Dañado":
        modelos_danados.append(traje)
    pila_aux.append(traje)

while pila_aux:
    pila_trajes.append(pila_aux.pop())

print("Modelos dañados:")
for traje in modelos_danados:
    print("-", traje["modelo"], "en", traje["pelicula"])

print("Modelos destruidos eliminados:")
pila_temporal = []

while pila_trajes:
    traje = pila_trajes.pop()
    if traje["estado"] == "Destruido":
        print("-", traje["modelo"])
    else:
        pila_temporal.append(traje)

while pila_temporal:
    pila_trajes.append(pila_temporal.pop())

existe = False
for traje in pila_trajes:
    if traje["modelo"] == "Mark LXXXV" and traje["pelicula"] == "Avengers: Endgame":
        existe = True
        break

if not existe:
    pila_trajes.append({
        "modelo": "Mark LXXXV",
        "pelicula": "Avengers: Endgame",
        "estado": "Impecable"
    })
    print("Modelo Mark LXXXV agregado.")
else:
    print("Modelo Mark LXXXV ya estaba cargado para esa película.")

print("Trajes usados en Spider-Man: Homecoming y Captain America: Civil War:")
for traje in pila_trajes:
    if traje["pelicula"] in ["Spider-Man: Homecoming", "Captain America: Civil War"]:
        print("-", traje["modelo"], "en", traje["pelicula"])
