from grafo import *

g1 = Grafo(['A','B','C','D','E'], {'1':'A-B','2':'A-C','3':'A-D','4':'C-D'})


print(g1.dfs_generator('E'))