import unittest
from grafo import *

class TesteDFS(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})

        # Grafo do roteiro 2
        self.g_r2 = Grafo(['A','B','C','D','E','F','G','H','I','J','K'], {'1':'A-B','2':'A-G','3':'A-J','4':'K-G','5':'K-J','6':'J-G','7':'J-I','8':'I-G','9':'G-H','10':'H-F','11':'F-B','12':'B-G','13':'B-C','14':'C-D','15':'D-E','16':'D-B','17':'B-E'})

        self.g_2 = Grafo(['A','B','C','D','E','F','G'], {'1':'A-F','2':'F-E','3':'E-C','4':'C-B','5':'C-A','6':'B-A','7':'B-A','8':'F-G','9':'A-G','10':'G-D'})

        # Grafo de arvore binaria completa
        self.g_a  = Grafo(['A','B','C','D','E','F','G'],{'1':'A-B','2':'A-C','3':'B-D','4':'B-E','5':'C-F','6':'C-G'})

        self.casinha = Grafo(['AA','B','C','D','E','FF','G'], {'1':'AA-B','2':'B-FF','3':'FF-C','4':'B-E','5':'E-D','6':'E-G','7':'C-D'})

    def testDFS(self):
        self.assertListEqual(['K', '4', 'G', '2', 'A', '1', 'B', '11', 'F', '10', 'H', '6', 'J', '7', 'I', '13', 'C', '14', 'D', '15', 'E'], self.g_r2.dfs_generator('K'))
        self.assertListEqual(['J', 'a1', 'C', 'a2', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'], self.g_p.dfs_generator('J'))


        self.assertListEqual(['A', '1', 'B', '3', 'D', '4', 'E', '2', 'C', '5', 'F', '6', 'G'], self.g_a.dfs_generator('A'))
        self.assertListEqual(['E', '4', 'B', '1', 'A', '2', 'C', '5', 'F', '6', 'G', '3', 'D'], self.g_a.dfs_generator('E'))

        
        self.assertListEqual(['J', 'a1', 'C', 'a2', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'], self.g_p.dfs_generator('J'))
        self.assertListEqual(['M', 'a6', 'C', 'a1', 'J', 'a2', 'E', 'a4', 'P', 'a7', 'T', 'a9', 'Z'], self.g_p.dfs_generator('M'))


        self.assertListEqual(['AA', '1', 'B', '2', 'FF', '3', 'C', '7', 'D', '5', 'E', '6', 'G'], self.casinha.dfs_generator('AA'))
        self.assertListEqual(['G', '6', 'E', '4', 'B', '1', 'AA', '2', 'FF', '3', 'C', '7', 'D'], self.casinha.dfs_generator('G'))

