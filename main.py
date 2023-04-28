import tkinter as tk
from tkinter import messagebox
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

def agregar_vertice():
    vertice = entry_vertice.get()
    if vertice:
        vertices.append(vertice)
        entry_vertice.delete(0, tk.END)
        actualizar_listas()

def agregar_arista():
    origen = entry_origen.get()
    destino = entry_destino.get()
    peso = entry_peso.get()
    if origen and destino and peso:
        aristas.append((origen, destino, int(peso)))
        entry_origen.delete(0, tk.END)
        entry_destino.delete(0, tk.END)
        entry_peso.delete(0, tk.END)
        actualizar_listas()

def actualizar_listas():
    lista_vertices.delete(0, tk.END)
    lista_aristas.delete(0, tk.END)

    for v in vertices:
        lista_vertices.insert(tk.END, v)

    for a in aristas:
        lista_aristas.insert(tk.END, f"{a[0]} - {a[1]} (Peso: {a[2]})")
def calcular_mst():
    if not vertices or not aristas:
        messagebox.showerror("Error", "Por favor, ingrese al menos un vértice y una arista.")
        return

    grafo_original.add_nodes_from(vertices)
    grafo_original.add_weighted_edges_from(aristas)

    mst = kruskal_algorithm(vertices, aristas)
    dibujar_grafo(grafo_original, 'grafo_original')
    dibujar_grafo(mst, 'arbol_cubrimiento_minimo')

    messagebox.showinfo("Información", "Se calcularon y dibujaron el grafo original y el MST.")

app = tk.Tk()
app.title("Algoritmo de Kruskal")

vertices = []
aristas = []
grafo_original = nx.Graph()

label_vertice = tk.Label(app, text="Vértice:")
entry_vertice = tk.Entry(app)
button_vertice = tk.Button(app, text="Agregar vértice", command=agregar_vertice)

label_origen = tk.Label(app, text="Arista origen:")
entry_origen = tk.Entry(app)
label_destino = tk.Label(app, text="Arista destino:")
entry_destino = tk.Entry(app)
label_peso = tk.Label(app, text="Peso:")
entry_peso = tk.Entry(app)
button_arista = tk.Button(app, text="Agregar arista", command=agregar_arista)

button_calcular = tk.Button(app, text="Calcular MST", command=calcular_mst)
label_lista_vertices = tk.Label(app, text="Vértices:")
label_lista_vertices.grid(row=5, column=0)
lista_vertices = tk.Listbox(app)
lista_vertices.grid(row=6, column=0, rowspan=2)

label_lista_aristas = tk.Label(app, text="Aristas:")
label_lista_aristas.grid(row=5, column=1)
lista_aristas = tk.Listbox(app)
lista_aristas.grid(row=6, column=1, rowspan=2)

label_vertice.grid(row=0, column=0)
entry_vertice.grid(row=0, column=1)
button_vertice.grid(row=0, column=2)

label_origen.grid(row=1, column=0)
entry_origen.grid(row=1, column=1)
label_destino.grid(row=2, column=0)
entry_destino.grid(row=2, column=1)
label_peso.grid(row=3, column=0)
entry_peso.grid(row=3, column=1)
button_arista.grid(row=3, column=2)

button_calcular.grid(row=4, column=1)

app.mainloop()