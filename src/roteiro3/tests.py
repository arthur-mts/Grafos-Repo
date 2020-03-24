import unittest

from grafo import *


class Test(unittest.TestCase):
    def setUp(self):
        # Grafo da Paraiba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {
                         'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'})

        self.g_a = Grafo(N=["A", "B", "C", "D", "E", "F", "G"],
                         A={
                         "1": "A-B", "2": "B-C", "3": "B-D",
                         "4": "A-E", "5": "E-F", "6": "E-G"})

        self.g_c = Grafo(N=["A", "B", "C", "D", "E", "F", "G", "H", "I"], A={
            "1": "A-B", "2": "B-D", "3": "B-C", "4": "C-D", "5": "C-E", "6": "D-G", "7": "E-F", "8": "F-G", "9": "E-H", "10": "F-H", "11": "G-H", "12": "H-I"})

        # Grafo desconexo
        self.gdisc = Grafo(N=["A", "B", "C", "D"], A={
            "1": "A-B", "2": "A-C", "3": "B-C"})

        # Grafo desconexo valido
        self.g_d = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                         {'1': 'A-B', '2': 'B-C', '3': 'C-D', '4': 'B-D', '5': 'A-C', '6': 'E-F', '7': 'F-G', '8': 'G-J', '9': 'J-I', '10': 'I-G'})

        # Grafo único
        self.g_u = Grafo(['A'])

        self.g_u_d = Grafo(['A', 'B'], {'1': 'A-A'})

        # Grafo sem ciclo

        self.g_s_c = Grafo(['A', 'B', 'C'], {'1': 'A-B', '2': 'B-C'})

    def testCaminho(self):
        self.assertFalse(self.gdisc.caminho(4))
        self.assertFalse(self.gdisc.caminho(3))
        self.assertListEqual(self.gdisc.caminho(2), ['A', '1', 'B', '3', 'C'])

        self.assertFalse(self.g_d.caminho(0))
        self.assertFalse(self.g_d.caminho(-1))

        self.assertListEqual(self.g_d.caminho(
            4), ['E', '6', 'F', '7', 'G', '8', 'J', '9', 'I'])

        self.assertFalse(self.g_d.caminho(12))
        self.assertFalse(self.g_d.caminho(8))
        self.assertFalse(self.g_d.caminho(5))

        self.assertListEqual(self.g_p.caminho(
            3), ['J', 'a1', 'C', 'a6', 'M', 'a8', 'T'])
        self.assertFalse(self.g_p.caminho(5))

        self.assertFalse(self.g_u.caminho(1))

    def testConexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_a.conexo())

        self.assertFalse(self.g_d.conexo())
        self.assertTrue(self.g_c.conexo())

        self.assertFalse(self.g_u.conexo())

        self.assertFalse(self.g_u_d.conexo())

    def testCiclo(self):
        self.assertTrue(self.g_p.ha_ciclo())
        self.assertTrue(self.g_u_d.ha_ciclo())
        self.assertTrue(self.gdisc.ha_ciclo())
        self.assertFalse(self.g_s_c.ha_ciclo())

        self.assertFalse(self.g_u.ha_ciclo())
