from grafo_lib import Grafo

from grafo_test import TestGrafo


vertices = ['J','C','E','P','M','T','Z']

grafoPB = Grafo(V=vertices)


grafoPB.adicionaAresta('C-E')
grafoPB.adicionaAresta('C-E')
grafoPB.adicionaAresta('C-P')
grafoPB.adicionaAresta('C-P')
grafoPB.adicionaAresta('C-M')
grafoPB.adicionaAresta('C-T')
grafoPB.adicionaAresta('M-T')
grafoPB.adicionaAresta('T-Z')
grafoPB.adicionaAresta('J-C')



g_c = Grafo(['J', 'C', 'E', 'P'])
g_c.adicionaAresta('J-C')
g_c.adicionaAresta('J-E')
g_c.adicionaAresta('J-P')
g_c.adicionaAresta('C-E')
g_c.adicionaAresta('C-P')
g_c.adicionaAresta('E-P')

print(g_c.eh_completo())