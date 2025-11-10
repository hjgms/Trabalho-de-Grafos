def criar_grafo():
    return [], []

def inserir_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        for linha in matriz:
            linha.append(0)
        matriz.append([0] * len(vertices))

def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)
    i, j = vertices.index(origem), vertices.index(destino)
    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1

def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        return
    i = vertices.index(vertice)
    matriz.pop(i)
    for linha in matriz:
        linha.pop(i)
    vertices.remove(vertice)

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem in vertices and destino in vertices:
        i, j = vertices.index(origem), vertices.index(destino)
        matriz[i][j] = 0
        if nao_direcionado:
            matriz[j][i] = 0

def existe_aresta(matriz, vertices, origem, destino):
    if origem in vertices and destino in vertices:
        i, j = vertices.index(origem), vertices.index(destino)
        return matriz[i][j] == 1
    return False

def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []
    i = vertices.index(vertice)
    return [vertices[j] for j in range(len(vertices)) if matriz[i][j] == 1]

def grau_vertices(matriz, vertices):
    graus = {}
    for i, v in enumerate(vertices):
        saida = sum(matriz[i])
        entrada = sum(linha[i] for linha in matriz)
        graus[v] = {'saida': saida, 'entrada': entrada, 'total': saida + entrada}
    return graus

def percurso_valido(matriz, vertices, caminho):
    for i in range(len(caminho) - 1):
        if not existe_aresta(matriz, vertices, caminho[i], caminho[i + 1]):
            return False
    return True

def listar_vizinhos(matriz, vertices, vertice):
    print(f"Vizinhos de {vertice}: {vizinhos(matriz, vertices, vertice)}")

def exibir_grafo(matriz, vertices):
    print("  ", " ".join(vertices))
    for i, v in enumerate(vertices):
        print(v, " ".join(map(str, matriz[i])))

def main():
    matriz, vertices = criar_grafo()
    while True:
        print("\n1 - Mostrar Grafo\n2 - Inserir Vértice\n3 - Inserir Aresta\n4 - Remover Vértice\n5 - Remover Aresta\n6 - Grau dos Vértices\n7 - Verificar Aresta\n8 - Listar Vizinhos\n9 - Verificar Percurso\n0 - Sair")
        op = input("Escolha: ")
        if op == '1':
            exibir_grafo(matriz, vertices)
        elif op == '2':
            v = input("Vértice: ")
            inserir_vertice(matriz, vertices, v)
        elif op == '3':
            o, d = input("Origem Destino: ").split()
            inserir_aresta(matriz, vertices, o, d, True)
        elif op == '4':
            v = input("Vértice: ")
            remover_vertice(matriz, vertices, v)
        elif op == '5':
            o, d = input("Origem Destino: ").split()
            remover_aresta(matriz, vertices, o, d, True)
        elif op == '6':
            print(grau_vertices(matriz, vertices))
        elif op == '7':
            o, d = input("Origem Destino: ").split()
            print(existe_aresta(matriz, vertices, o, d))
        elif op == '8':
            v = input("Vértice: ")
            listar_vizinhos(matriz, vertices, v)
        elif op == '9':
            caminho = input("Caminho (v1 v2 ...): ").split()
            print(percurso_valido(matriz, vertices, caminho))
        elif op == '0':
            break

if __name__ == "__main__":
    main()
