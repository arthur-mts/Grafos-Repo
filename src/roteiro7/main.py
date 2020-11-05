from grafo_adj_dir import Grafo

grafo0 = Grafo(['A', 'B', 'C'])
grafo0.adiciona_aresta('A-B')
grafo0.adiciona_aresta('B-C')
grafo0.adiciona_aresta('C-A')

a = grafo0.menor_caminho_drone("A", "G", 10000, 50000, ["D", "E"])
