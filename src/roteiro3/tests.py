import unittest

from grafo import *


class Test(unittest.TestCase):
    def setUp(self):
        # Grafo da Paraiba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {
                         'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'})

        self.g_a = Grafo(N=["A", "B", "C", "D", "E", "F", "G"], A={
                         "1": "A-B", "2": "B-C", "3": "B-D", "4": "A-E", "5": "E-F", "6": "E-G"})

        self.g_c = Grafo(N=["A", "B", "C", "D", "E", "F", "G", "H", "I"], A={
            "1": "A-B", "2": "B-D", "3": "B-C", "4": "C-D", "5": "C-E", "6": "D-G", "7": "E-F", "8": "F-G", "9": "E-H", "10": "F-H", "11": "G-H", "12": "H-I"})

        # Grafo disconexto
        self.gdisc = Grafo(N=["A", "B", "C", "D"], A={
            "1": "A-B", "2": "A-C", "3": "B-C"})

    def testCaminho(self):
        self.assertFalse(self.gdisc.caminho(4))
        self.assertFalse(self.gdisc.caminho(3))
        self.assertListEqual(self.gdisc.caminho(2), ['A', '1', 'B', '3', 'C'])
