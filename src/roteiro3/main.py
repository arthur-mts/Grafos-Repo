from grafo import *

g1 = Grafo(N=["A","B","C","D","E","F","G","H","I","Z"],A={"1":"A-B","2":"B-D","3":"B-C","4":"C-D","5":"C-E","6":"D-G","7":"E-F","8":"F-G","9":"E-H","10":"F-H","11":"G-H","12":"H-I"})


print(g1.caminho(8))

print(g1.conexo())