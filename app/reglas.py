TRANCONES = [
    ("PuntoC", "PuntoA"),
    ("PuntoG", "PuntoH")
]

def filtrar_trancones(conexiones):
    return [
        (origen, destino, costo)
        for origen, destino, costo in conexiones
        if (origen, destino) not in TRANCONES and (destino, origen) not in TRANCONES
    ]