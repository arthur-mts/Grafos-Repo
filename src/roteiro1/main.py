from grafo import Grafo
from quests import *
from grafo_test import TestGrafo
# Q1: Construa o grafo da Paraíba usando o módulo grafo.py 
# disponibilizado aqui e o imprima na saída padrão.
# Use import para incluir grafo.py em seu próprio módulo:

grafoPB = Grafo(["C", "J", "E", "P", "M", "T", "Z"])

grafoPB.adicionaAresta("a1","J-C")

grafoPB.adicionaAresta("a2","C-E")
grafoPB.adicionaAresta("a3","C-E")
grafoPB.adicionaAresta("a4","C-P")
grafoPB.adicionaAresta("a5","C-P")
grafoPB.adicionaAresta("a6","C-M")
grafoPB.adicionaAresta("a7","C-T")

grafoPB.adicionaAresta("a8","M-T")
grafoPB.adicionaAresta("a9","T-Z")

# Q2: Crie funções em Python para satisfazer os seguintes questionamentos:

# a)
print("Resposta da A: ",getVerticesNotAdj(grafoPB))

# b)
print("Resposta da B: ",verticeLaco(grafoPB))

# c)
print("Resposta da C: ",arestasParalelas(grafoPB))

# d)
print("Resposta da D, para o vertice C: ",contGrau(grafoPB, "C"))
print("Resposta da D, para o vertice M: ",contGrau(grafoPB, "M"))

# e)
print("Resposta da E, para o vertice J: ", grau(grafoPB, "J"))
print("Resposta da E, para o vertice C: ", grau(grafoPB, "C"))

# f)

print("Resposta da F: ", ehCompleto(grafoPB))