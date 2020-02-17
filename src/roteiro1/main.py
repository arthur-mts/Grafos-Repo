# -*- coding: utf-8 -*-

from grafo import Grafo
from quests import *
from grafo_test import TestGrafo

g_l4 = Grafo(['D'], {'a2':'D-D'})

g_l4.eh_completo()

teste = TestGrafo()

teste.setUp()

teste.test_vertices_nao_adjacentes()

teste.test_ha_laco()

teste.test_grau()

teste.test_arestas_ha_paralelas()

teste.test_arestas_sobre_vertice()

teste.test_eh_completo()
