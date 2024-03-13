import networkx as nx
import matplotlib.pyplot as plt


class Grafo:

    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def adicionarAresta(self, origem, destino, valorAresta):
        self.grafo.append([origem, destino, valorAresta])

    def imprimirDistancias(self, dist):
        print("Vértice\tDistância a partir da Origem")
        for i in range(self.V):
            print("{0}\t\t{1}".format(chr(ord('A') + i), dist[i]))

    def caminhoMinimo(self, pai, destino):
        caminho = [destino]
        while pai[ord(destino) - ord('A')] != -1:
            destino = chr(pai[ord(destino) - ord('A')] + ord('A'))
            caminho.insert(0, destino)
        return ''.join(caminho)

    def BellmanFord(self, partida, destino):
        dist = [float("Inf")] * self.V
        pai = [-1] * self.V
        dist[partida] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.grafo:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pai[v] = u

        self.imprimirDistancias(dist)

        caminho = self.caminhoMinimo(pai, destino)
        print(f"Caminho mínimo de {chr(ord('A') + partida)} para {destino}: {caminho}")

        G = nx.DiGraph()

        for u, v, w in self.grafo:
            G.add_edge(chr(ord('A') + u), chr(ord('A') + v), weight=w)

        pos = {'A': (0, 0), 'B': (2, 2), 'C': (2, -2), 'D': (4, -2), 'E': (6, -1), 'F': (5, 2)}

        # Plotar o grafo
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10,
                edge_color='gray', width=2, arrowsize=15)

        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

        plt.show()


g = Grafo(5)
g.adicionarAresta(0, 1, 9)
g.adicionarAresta(0, 2, 7)
g.adicionarAresta(1, 4, 2)
g.adicionarAresta(2, 3, 2)
g.adicionarAresta(3, 1, -3)
g.adicionarAresta(3, 4, -2)

g.BellmanFord(0, 'E')