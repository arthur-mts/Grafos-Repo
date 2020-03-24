from grafo import *
# Grafo da Paraiba
g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {
    'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'})

g_a = Grafo(N=["A", "B", "C", "D", "E", "F", "G"],
            A={
    "1": "A-B", "2": "B-C", "3": "B-D",
    "4": "A-E", "5": "E-F", "6": "E-G"})

g_c = Grafo(N=["A", "B", "C", "D", "E", "F", "G", "H", "I"], A={
    "1": "A-B", "2": "B-D", "3": "B-C", "4": "C-D", "5": "C-E", "6": "D-G", "7": "E-F", "8": "F-G", "9": "E-H", "10": "F-H", "11": "G-H", "12": "H-I"})

# Grafo desconexo
gdisc = Grafo(N=["A", "B", "C", "D"], A={
    "1": "A-B", "2": "A-C", "3": "B-C"})

# Grafo desconexo valido
g_d = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            {'1': 'A-B', '2': 'B-C', '3': 'C-D', '4': 'B-D', '5': 'A-C', '6': 'E-F', '7': 'F-G', '8': 'G-J', '9': 'J-I', '10': 'I-G'})

# Grafo único
g_u = Grafo(['A'])

g_u_d = Grafo(['A', 'B'], {'1': 'A-A'})

g_s_c = Grafo(['A', 'B', 'C'], {'1': 'A-B', '2': 'B-C'})
print(g_u.ha_ciclo())
