## Q2
## A) Encontre todos os pares de vértices não adjacentes.

def getVerticesNotAdj(grafo):
    ## Iniciando lista que conterá os pares adjacentes
    paresNAdj = []
    ## Percorrendo o conjunto de vértices, chamando-os de node
    for node in grafo.N:
        ## A estrutura set não armazena dois elementos iguais
        ## será nosso conjunto de adjacentes, a fim de evitar vértices repetidos
        verticesAdj = set()

        ## Percorrendo o conjunto de arestas para cada um dos vértices
        for aresta in grafo.A:
            ## Procurando os vértices adjacentes dentro de cada 
            ## subconjunto de A(aresta) em relação ao vértice atual
            if(node in grafo.A[aresta]):
                verticeAdj = grafo.A[aresta]
                ## Removendo o vértice que está conectado com o atual da repetição
                ## Ex: J-C --> C
                verticeAdj = verticeAdj.replace(node, "").replace("-", "")
                ## Adicionando o vértice adjacente, já tratado, ao conjunto de adjacentes
                verticesAdj.add(verticeAdj)
        
        verticesNAdj = [node + "-" + v for v in grafo.N if v not in list(verticesAdj) and v!=node]
        paresNAdj.extend(verticesNAdj)
    
    ## Ex: Se considerarmos que J-M é o mesmo par que M-J,
    ## é necessários excluirmos os pares palíndromos:
    for par in paresNAdj:
        if(par[::-1] in paresNAdj):
            # Removemos o par palíndromo
            paresNAdj.remove(par[::-1])    

    # Retorno da nossa lista de pares não adjacentes
    return paresNAdj
        


# B) Há algum vértice adjacente a ele mesmo? (Retorne True ou False)
def verticeLaco(grafo):
    ## Para cada vértice vemos suas arestas
    for vertice in grafo.A:
        # Se a função da aresta é palíndromo, ela é um laço
        # sedo um laço, sabemos que é adjacente a si mesmo
        if(grafo.A[vertice] == grafo.A[vertice][::-1]):
            return True
            
    return False

# C) Há arestas paralelas? (Retorne True ou False)
def arestasParalelas(grafo):
    # Transformamos os valores do dicionário de arestas em uma lista
    allVertices = list(grafo.A.values())
    # Percorremos os vertices vendo se possui mais de uma conexão igual(aresta)
    # ou vendo se possui uma aresta palindromo, que também seria paralela
    for vertice in allVertices:
        if(allVertices.count(vertice) > 1 or vertice[::-1] in allVertices):
            return True

    return False


# D) Qual o grau de um vértice arbitrário?
def contGrau(grafo, verticeC):
    #iniciamos nosso contador para grau
    count = 0

    for aresta in grafo.A:
        # Percorremos os vértices e verificamos quantas vezes
        # o vértice passado se repete no conjunto de arestas
        if(verticeC in grafo.A[aresta]):
            count+= 1 
    return count


# E) Quais arestas incidem sobre um vértice N arbitrário?
def grau(grafo, verticeC):
    return [aresta for aresta in grafo.A if verticeC in grafo.A[aresta]]

# F) Esse grafo é completo?

# G) Para essa atividade foi criado um conjunto de casos de teste. Use-o para testar seu módulo em Python.
        #https://drive.google.com/file/d/1fjPhfXAIe3AoawVogPJEdW978-BubOvY/view?usp=sharing
        
# H) As funções devem ser criadas dentro do arquivo grafo.py

