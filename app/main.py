import matplotlib.pyplot as plt
import networkx as nx
import heapq

from base_conocimiento import CONEXIONES
from algoritmo_a_star import a_star, heuristica_nula
from reglas import filtrar_trancones

def plot_route(conexiones, ruta):
    G = nx.Graph()
    for origen, destino, peso in conexiones:
        G.add_edge(origen, destino, weight=peso)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    if ruta:
        ruta_edges = list(zip(ruta, ruta[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, edge_color='red', width=3)

    plt.title("Visualización de la Ruta Óptima (evitando trancones)")
    plt.show()

def main():
    conexiones_filtradas = filtrar_trancones(CONEXIONES)
    
    origen = "PuntoA"
    destino = "PuntoL"
    ruta, costo = a_star(origen, destino, conexiones_filtradas, heuristica_nula)

    if ruta:
        print(f"Ruta óptima encontrada de {origen} a {destino}: {ruta}")
        print(f"Costo total: {costo}")
        plot_route(conexiones_filtradas, ruta)
    else:
        print("No se encontró ruta (posible trancón en todos los caminos).")

if __name__ == "__main__":
    main()