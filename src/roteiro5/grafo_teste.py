import unittest
from grafo_lib import Grafo


# python3 -m unittest grafo_teste.GrafoTeste.testCaminhoEuleriano
class GrafoTeste(unittest.TestCase):
    def setUp(self):
        self.grafo1 = Grafo(['A','B','C','D'])
        self.grafo1.adicionaAresta('A-B')
        self.grafo1.adicionaAresta('A-B')
        self.grafo1.adicionaAresta('A-B')
        self.grafo1.adicionaAresta('B-D')
        self.grafo1.adicionaAresta('D-C')
        self.grafo1.adicionaAresta('C-A')

        self.grafo2 = Grafo(['A', 'B', 'C','D'])
        self.grafo2.adicionaAresta('A-B')
        self.grafo2.adicionaAresta('B-D')
        self.grafo2.adicionaAresta('A-C')
        self.grafo2.adicionaAresta('C-B')

        self.grafo3 = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])
        self.grafo3.adicionaAresta('D-G')
        self.grafo3.adicionaAresta('B-G')
        self.grafo3.adicionaAresta('E-B')
        self.grafo3.adicionaAresta('C-E')
        self.grafo3.adicionaAresta('D-A')
        self.grafo3.adicionaAresta('D-C')
        self.grafo3.adicionaAresta('D-F')
        self.grafo3.adicionaAresta('A-C')
        self.grafo3.adicionaAresta('C-F')
        self.grafo3.adicionaAresta('E-G')
        self.grafo3.adicionaAresta('E-H')
        self.grafo3.adicionaAresta('H-G')




        self.grafo4 = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])
        self.grafo4.adicionaAresta('D-G')
        self.grafo4.adicionaAresta('B-G')
        self.grafo4.adicionaAresta('E-B')
        self.grafo4.adicionaAresta('C-E')
        self.grafo4.adicionaAresta('D-A')
        self.grafo4.adicionaAresta('D-C')
        self.grafo4.adicionaAresta('D-F')
        self.grafo4.adicionaAresta('A-C')
        self.grafo4.adicionaAresta('C-F')
        self.grafo4.adicionaAresta('E-G')
        self.grafo4.adicionaAresta('E-H')
        self.grafo4.adicionaAresta('H-G')
        self.grafo4.adicionaAresta('A-H')

    def testCaminhoEuleriano(self):
        self.assertEqual(['A-B', 'A-B', 'A-B', 'B-D', 'C-D', 'A-C'], self.grafo1.caminhoEuleriano())
        self.assertEqual(['A-B', 'A-C', 'B-C', 'B-D'], self.grafo2.caminhoEuleriano())
        self.assertEqual(['D-C', 'C-A', 'D-A', 'D-F', 'C-F', 'C-E', 'E-H', 'H-G', 'E-G', 'E-B', 'G-B', 'D-G'], self.grafo3.caminhoEuleriano())
        self.assertEqual(['D-A', 'D-C', 'C-A', 'A-H', 'E-H', 'C-E', 'C-F', 'D-F', 'D-G', 'E-G', 'E-B', 'G-B', 'H-G'], self.grafo4.caminhoEuleriano())