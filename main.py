import networkx as nx
from graphviz import Digraph
import heapq

def kruskal_algorithm(vertices, aristas):
    grafo = nx.Graph()
    grafo.add_nodes_from(vertices)
    grafo.add_weighted_edges_from(aristas)
    
    mst = nx.Graph()
    mst.add_nodes_from(vertices)

    aristas = [(w, u, v) for u, v, w in grafo.edges(data='weight')]
    heapq.heapify(aristas)

    union_find = nx.utils.union_find.UnionFind(vertices)

    while aristas and len(mst.edges) < len(vertices) - 1:
        w, u, v = heapq.heappop(aristas)

        if union_find[u] != union_find[v]:
            mst.add_edge(u, v, weight=w)
            union_find.union(u, v)

    return mst

def dibujar_grafo(grafo, nombre):
    dot = Digraph(name=nombre, format='png')
    for u, v, w in grafo.edges(data=True):
        dot.edge(str(u), str(v), label=str(w['weight']))

    dot.view()

# Ingresar los vértices y las aristas manualmente
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
aristas = [
    ('A', 'B', 7),
    ('A', 'D', 5),
    ('B', 'C', 8),
    ('B', 'D', 9),
    ('B', 'E', 7),
    ('C', 'E', 5),
    ('D', 'E', 15),
    ('D', 'F', 6),
    ('E', 'F', 8),
    ('E', 'G', 9),
    ('F', 'G', 11)
]

# Crear un grafo con los vértices y aristas ingresados manualmente
grafo_original = nx.Graph()
grafo_original.add_nodes_from(vertices)
grafo_original.add_weighted_edges_from(aristas)

# Ejecutar el algoritmo de Kruskal
mst = kruskal_algorithm(vertices, aristas)

# Dibujar el grafo original y el MST
dibujar_grafo(grafo_original, 'grafo_original')
dibujar_grafo(mst, 'arbol_cubrimiento_minimo')