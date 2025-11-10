def criar_grafo():
    return {}

def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []

def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)

def vizinhos(grafo, vertice):
    return grafo.get(vertice, [])

def listar_vizinhos(grafo, vertice):
    print(f"Vizinhos de {vertice}: {vizinhos(grafo, vertice)}")

def exibir_grafo(grafo):
    for v in grafo:
        print(f"{v} -> {grafo[v]}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)

def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        return
    for v in list(grafo.keys()):
        if vertice in grafo[v]:
            grafo[v].remove(vertice)
    del grafo[vertice]

def existe_aresta(grafo, origem, destino):
    return origem in grafo and destino in grafo[origem]

def grau_vertices(grafo):
    graus = {}
    for v in grafo:
        saida = len(grafo[v])
        entrada = sum(v in grafo[u] for u in grafo)
        graus[v] = {'saida': saida, 'entrada': entrada, 'total': saida + entrada}
    return graus

def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if not existe_aresta(grafo, caminho[i], caminho[i + 1]):
            return False
    return True

def main():
    grafo = criar_grafo()
    while True:
        print("\n1 - Mostrar Grafo\n2 - Inserir Vértice\n3 - Inserir Aresta\n4 - Remover Vértice\n5 - Remover Aresta\n6 - Grau dos Vértices\n7 - Verificar Aresta\n8 - Listar Vizinhos\n9 - Verificar Percurso\n0 - Sair")
        op = input("Escolha: ")
        if op == '1':
            exibir_grafo(grafo)
        elif op == '2':
            v = input("Vértice: ")
            inserir_vertice(grafo, v)
        elif op == '3':
            o, d = input("Origem Destino: ").split()
            inserir_aresta(grafo, o, d, True)
        elif op == '4':
            v = input("Vértice: ")
            remover_vertice(grafo, v)
        elif op == '5':
            o, d = input("Origem Destino: ").split()
            remover_aresta(grafo, o, d, True)
        elif op == '6':
            print(grau_vertices(grafo))
        elif op == '7':
            o, d = input("Origem Destino: ").split()
            print(existe_aresta(grafo, o, d))
        elif op == '8':
            v = input("Vértice: ")
            listar_vizinhos(grafo, v)
        elif op == '9':
            caminho = input("Caminho (v1 v2 ...): ").split()
            print(percurso_valido(grafo, caminho))
        elif op == '0':
            break

if __name__ == "__main__":
    main()
