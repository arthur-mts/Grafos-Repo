## ARTHUR MAURÍCIO
## JONATAS DUARTE

import unittest

from grafo_adj_dir import Grafo

class TesteDrone(unittest.TestCase):
    def setUp(self):
        #grafo 1
        self.g1 = Grafo(N=['A','B','C','D'])
        self.g1.adiciona_aresta('A-B')
        self.g1.adiciona_aresta('A-C')
        self.g1.adiciona_aresta('C-B')
        self.g1.adiciona_aresta('C-D')
        self.g1.adiciona_aresta('D-B')
        
        #grafo 2
        self.g2 = Grafo(N=['A','B'])
        self.g2.adiciona_aresta('A-B')
       
        #grafo 3
        self.g3 = Grafo(N=['A','B','C','D', 'E'])
        self.g3.adiciona_aresta('A-B')
        self.g3.adiciona_aresta('A-C')
        self.g3.adiciona_aresta('C-B')
        self.g3.adiciona_aresta('C-D')
        self.g3.adiciona_aresta('D-E')
        self.g3.adiciona_aresta('B-E')

        #grafo 4
        self.g4 = Grafo(N=['A','B','C','D'])
        self.g4.adiciona_aresta('A-B')
        self.g4.adiciona_aresta('A-C')
        self.g4.adiciona_aresta('A-B')
        self.g4.adiciona_aresta('B-C')
        self.g4.adiciona_aresta('C-D')

        #grafo 5
        self.g5 = Grafo(N=['A','B','C','D', 'E', 'F'])
        self.g5.adiciona_aresta('A-B')
        self.g5.adiciona_aresta('A-D')
        self.g5.adiciona_aresta('B-C')
        self.g5.adiciona_aresta('B-E')
        self.g5.adiciona_aresta('C-D')
        self.g5.adiciona_aresta('D-F')
        self.g5.adiciona_aresta('E-F')


    def testeMenorCaminhoDrone(self):
        self.assertListEqual(self.g1.caminhoDrone('A', 'B', 2, 2, ['D']), ['A','B'])

        self.assertListEqual(self.g2.caminhoDrone('A', 'B', 1, 1, []), ['A', 'B'])

        self.assertListEqual(self.g3.caminhoDrone('A', 'E', 1, 2, ['B']), ['A','B','C'])

        self.assertListEqual(self.g4.caminhoDrone('A', 'D', 2, 2, ['B']), ['A','C','D'])

        self.assertListEqual(self.g4.caminhoDrone('A', 'D', 1, 2, ['B','C']), ['A','C','D'])

        self.assertListEqual(self.g5.caminhoDrone('A', 'F', 1, 1, ['B','C','D','E']), ['A','D','F'])
        