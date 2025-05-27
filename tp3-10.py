class Notificacion:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.hora} - {self.aplicacion}: {self.mensaje}"

def eliminar_facebook(cola):
    nueva_cola = []
    for noti in cola:
        if noti.aplicacion != "Facebook":
            nueva_cola.append(noti)
    return nueva_cola

def mostrar_twitter_python(cola):
    for noti in cola:
        if noti.aplicacion == "Twitter" and "Python" in noti.mensaje:
            print(noti)

def notificaciones_en_rango(cola):
    pila = []
    for noti in cola:
        if "11:43" <= noti.hora <= "15:57":
            pila.append(noti)
    print("Cantidad:", len(pila))

cola_notificaciones = [
    Notificacion("10:15", "Instagram", "Nueva historia de un amigo"),
    Notificacion("11:45", "Twitter", "Python es genial"),
    Notificacion("12:30", "Facebook", "Tienes un nuevo amigo"),
    Notificacion("13:15", "Twitter", "Python y Django"),
    Notificacion("14:00", "Instagram", "Publicación nueva de alguien"),
    Notificacion("16:10", "Facebook", "Recordatorio de evento"),
    Notificacion("17:30", "Twitter", "Noticias de programación"),
]

cola_notificaciones = eliminar_facebook(cola_notificaciones)
mostrar_twitter_python(cola_notificaciones)
notificaciones_en_rango(cola_notificaciones)
