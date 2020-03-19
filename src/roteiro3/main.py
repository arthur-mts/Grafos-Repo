from grafo import *

g1 = Grafo(N=["A", "B", "C", "D", "E", "F", "G", "H", "I"], A={
    "1": "A-B", "2": "B-D", "3": "B-C", "4": "C-D", "5":
    "C-E", "6": "D-G", "7": "E-F", "8": "F-G", "9": "E-H",
    "10": "F-H", "11": "G-H", "12": "H-I"})

g2 = Grafo(N=["A", "B", "C", "D", "E"], A={
    '1': 'A-B', '2': 'B-D', '3': 'A-C', '4': 'B-E', '5': 'C-E'})

g3 = Grafo(N=["1", "2", "3", "4", "5"], A={
           "A": "1-2", "B": "2-4", "C": "1-3", "D": "2-5"})
# print(g1.dfs_generator("Z"))
# print(g1.caminho(8))


# print(g1.conexo())
print(g1.ha_ciclo())
print(g2.ha_ciclo())
print(g3.ha_ciclo())
