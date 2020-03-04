from grafo import *

g_p = Grafo(N=['J','C','E','P','M','T','Z'], A={'a1': 'J-C', 'a2':'C-E','a3':'C-E','a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})

print(g_p.dfs_generator('J'))

# N = {J, C, E, P, M, T, Z}
# A = {a1, a2, a3, a4, a5, a6, a7, a8, a9}
# g(a1) = JC, g(a2) = CE, g(a3) = CE, g(a4) = CP, g(a5) = CP, g(a6) = CM, g(a7) = CT, g(a8) = MT, g(a9) = TZ


