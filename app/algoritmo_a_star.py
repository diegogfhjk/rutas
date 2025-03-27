import heapq

def a_star(inicio, meta, conexiones, heuristica):
    grafo = {}
    for origen, destino, costo in conexiones:
        grafo.setdefault(origen, []).append((destino, costo))
        grafo.setdefault(destino, []).append((origen, costo))

    cola = [(heuristica(inicio, meta), 0, inicio, [])]
    visitados = {}

    while cola:
        f, g, actual, camino = heapq.heappop(cola)
        if actual == meta:
            return camino + [actual], g
        if actual in visitados and visitados[actual] <= g:
            continue
        visitados[actual] = g
        for vecino, costo in grafo.get(actual, []):
            nuevo_g = g + costo
            nuevo_f = nuevo_g + heuristica(vecino, meta)
            heapq.heappush(cola, (nuevo_f, nuevo_g, vecino, camino + [actual]))

    return None, float("inf")

def heuristica_nula(nodo, meta):
    return 0