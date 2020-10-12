from grafo_lib import Grafo

grafo1 = Grafo(['A','B','C','D'])

grafo1.adicionaAresta('A-B')
grafo1.adicionaAresta('A-B')
grafo1.adicionaAresta('A-B')
grafo1.adicionaAresta('B-D')
grafo1.adicionaAresta('D-C')
grafo1.adicionaAresta('C-A')

print(grafo1.caminhoEuleriano())

grafo2 = Grafo(['A', 'B', 'C','D'])
grafo2.adicionaAresta('A-B')
grafo2.adicionaAresta('B-D')
grafo2.adicionaAresta('A-C')
grafo2.adicionaAresta('C-B')

grafo3 = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])

grafo3.adicionaAresta('D-G')
grafo3.adicionaAresta('B-G')
grafo3.adicionaAresta('E-B')
grafo3.adicionaAresta('C-E')
grafo3.adicionaAresta('D-A')
grafo3.adicionaAresta('D-C')
grafo3.adicionaAresta('D-F')
grafo3.adicionaAresta('A-C')
grafo3.adicionaAresta('C-F')
grafo3.adicionaAresta('E-G')
grafo3.adicionaAresta('E-H')
grafo3.adicionaAresta('H-G')


print(grafo3.caminhoEuleriano())


grafo4 = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])

grafo4.adicionaAresta('D-G')
grafo4.adicionaAresta('B-G')
grafo4.adicionaAresta('E-B')
grafo4.adicionaAresta('C-E')
grafo4.adicionaAresta('D-A')
grafo4.adicionaAresta('D-C')
grafo4.adicionaAresta('D-F')
grafo4.adicionaAresta('A-C')
grafo4.adicionaAresta('C-F')
grafo4.adicionaAresta('E-G')
grafo4.adicionaAresta('E-H')
grafo4.adicionaAresta('H-G')
grafo4.adicionaAresta('A-H')

print(grafo4.caminhoEuleriano())
