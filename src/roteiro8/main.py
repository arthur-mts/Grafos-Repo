from grafo_adj_dir import Grafo

g1 = Grafo(N=['A','B','C'])

g1.adiciona_aresta('A-B', 3)
g1.adiciona_aresta('A-C', 6)
g1.adiciona_aresta('B-C', 2)
print(g1)
print(g1.kruskalModificado())



# g2 = Grafo(N=['A','B','C','D','E','F','G','H'])
# g2.adiciona_aresta('A-B', 9)
# g2.adiciona_aresta('B-C', 6)
# g2.adiciona_aresta('C-D', 8)
# g2.adiciona_aresta('D-E', 14)
# g2.adiciona_aresta('E-C', 12)
# g2.adiciona_aresta('C-F', 8)
# g2.adiciona_aresta('E-F', 2)
# g2.adiciona_aresta('F-G', 1)
# g2.adiciona_aresta('F-H', 2)
# g2.adiciona_aresta('H-B', 7)
# g2.adiciona_aresta('G-A', 4)
# g2.adiciona_aresta('G-B', 10)
# print(g2)
# print(g2.primModificado())
