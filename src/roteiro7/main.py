from grafo_adj_dir import Grafo

g1 = Grafo(N=['A','B','C','D'])
g1.adiciona_aresta('A-B')
g1.adiciona_aresta('A-C')
g1.adiciona_aresta('C-B')
g1.adiciona_aresta('C-D')
g1.adiciona_aresta('D-B')

print(g1.caminhoDrone('A', 'B', 2, 2, ['D']))



g5 = Grafo(N=['A','B','C','D', 'E', 'F'])
g5.adiciona_aresta('A-B')
g5.adiciona_aresta('A-D')
g5.adiciona_aresta('B-C')
g5.adiciona_aresta('B-E')
g5.adiciona_aresta('C-D')
g5.adiciona_aresta('D-F')
g5.adiciona_aresta('E-F')

a = g5.caminhoDrone('A', 'F', 1, 1, ['B','C','D','E'])

print(a)