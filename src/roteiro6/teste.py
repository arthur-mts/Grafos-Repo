import unittest
from grafo_adj_dir import Grafo

# python3 -m unittest grafo_teste.GrafoTeste.testCaminhoEuleriano
class GrafoTeste(unittest.TestCase):
    def setUp(self):
        self.grafo0 = Grafo(['A','B','C'])
        self.grafo0.adiciona_aresta('A-B')
        self.grafo0.adiciona_aresta('B-C')
        self.grafo0.adiciona_aresta('C-A')

        self.grafo1 = Grafo(['A','B','C','D'])
        self.grafo1.adiciona_aresta('A-B')
        self.grafo1.adiciona_aresta('A-B')
        self.grafo1.adiciona_aresta('A-B')
        self.grafo1.adiciona_aresta('B-D')
        self.grafo1.adiciona_aresta('D-C')
        self.grafo1.adiciona_aresta('C-A')

        self.grafo2 = Grafo(['A', 'B', 'C','D'])
        self.grafo2.adiciona_aresta('A-B')
        self.grafo2.adiciona_aresta('B-D')
        self.grafo2.adiciona_aresta('A-C')
        self.grafo2.adiciona_aresta('C-B')

        self.grafo3 = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])
        self.grafo3.adiciona_aresta('D-G')
        self.grafo3.adiciona_aresta('B-G')
        self.grafo3.adiciona_aresta('E-B')
        self.grafo3.adiciona_aresta('C-E')
        self.grafo3.adiciona_aresta('D-A')
        self.grafo3.adiciona_aresta('D-C')
        self.grafo3.adiciona_aresta('D-F')
        self.grafo3.adiciona_aresta('A-C')
        self.grafo3.adiciona_aresta('C-F')
        self.grafo3.adiciona_aresta('E-G')
        self.grafo3.adiciona_aresta('E-H')
        self.grafo3.adiciona_aresta('H-G')




        self.grafo4 = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])
        self.grafo4.adiciona_aresta('D-G')
        self.grafo4.adiciona_aresta('B-G')
        self.grafo4.adiciona_aresta('E-B')
        self.grafo4.adiciona_aresta('C-E')
        self.grafo4.adiciona_aresta('D-A')
        self.grafo4.adiciona_aresta('D-C')
        self.grafo4.adiciona_aresta('D-F')
        self.grafo4.adiciona_aresta('A-C')
        self.grafo4.adiciona_aresta('C-F')
        self.grafo4.adiciona_aresta('E-G')
        self.grafo4.adiciona_aresta('E-H')
        self.grafo4.adiciona_aresta('H-G')
        self.grafo4.adiciona_aresta('A-H')

    def testWarshaw(self):
        self.assertEqual([[1, 1, 1], [1, 1, 1], [1, 1, 1]], self.grafo0.warshall())
        self.assertEqual([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], self.grafo1.warshall())
        self.assertEqual([[0, 1, 1, 1], [0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 0, 0]], self.grafo2.warshall())
        self.assertEqual([[0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]], self.grafo3.warshall())
        self.assertEqual([[0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]], self.grafo4.warshall())