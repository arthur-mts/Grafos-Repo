from grafo_adj_dir import Grafo

grafo0 = Grafo(['A','B','C'])
grafo0.adiciona_aresta('A-B')
grafo0.adiciona_aresta('B-C')
grafo0.adiciona_aresta('C-A')

grafo1 = Grafo(['A','B','C','D'])

print(grafo0.warshall())

grafo1.adiciona_aresta('A-B')
grafo1.adiciona_aresta('A-B')
grafo1.adiciona_aresta('A-B')
grafo1.adiciona_aresta('B-D')
grafo1.adiciona_aresta('D-C')
grafo1.adiciona_aresta('C-A')

print(grafo1.warshall())

grafo2 = Grafo(['A', 'B', 'C','D'])
grafo2.adiciona_aresta('A-B')
grafo2.adiciona_aresta('B-D')
grafo2.adiciona_aresta('A-C')
grafo2.adiciona_aresta('C-B')

print(grafo2.warshall())

grafo3 = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])

grafo3.adiciona_aresta('D-G')
grafo3.adiciona_aresta('B-G')
grafo3.adiciona_aresta('E-B')
grafo3.adiciona_aresta('C-E')
grafo3.adiciona_aresta('D-A')
grafo3.adiciona_aresta('D-C')
grafo3.adiciona_aresta('D-F')
grafo3.adiciona_aresta('A-C')
grafo3.adiciona_aresta('C-F')
grafo3.adiciona_aresta('E-G')
grafo3.adiciona_aresta('E-H')
grafo3.adiciona_aresta('H-G')

print(grafo3.warshall())

grafo4 = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])

grafo4.adiciona_aresta('D-G')
grafo4.adiciona_aresta('B-G')
grafo4.adiciona_aresta('E-B')
grafo4.adiciona_aresta('C-E')
grafo4.adiciona_aresta('D-A')
grafo4.adiciona_aresta('D-C')
grafo4.adiciona_aresta('D-F')
grafo4.adiciona_aresta('A-C')
grafo4.adiciona_aresta('C-F')
grafo4.adiciona_aresta('E-G')
grafo4.adiciona_aresta('E-H')
grafo4.adiciona_aresta('H-G')
grafo4.adiciona_aresta('A-H')

print(grafo4.warshall())