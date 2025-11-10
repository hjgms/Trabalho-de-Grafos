def criar_grafo():
    return [], []

def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)
    if [origem, destino] not in arestas:
        arestas.append([origem, destino])
    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])

def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])

def remover_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        return
    vertices.remove(vertice)
    arestas[:] = [a for a in arestas if vertice not in a]

def existe_aresta(arestas, origem, destino):
    return [origem, destino] in arestas

def vizinhos(vertices, arestas, vertice):
    return [d for (o, d) in arestas if o == vertice]

def grau_vertices(vertices, arestas):
    graus = {v: {'saida': 0, 'entrada': 0, 'total': 0} for v in vertices}
    for o, d in arestas:
        graus[o]['saida'] += 1
        graus[d]['entrada'] += 1
    for v in graus:
        graus[v]['total'] = graus[v]['entrada'] + graus[v]['saida']
    return graus

def percurso_valido(arestas, caminho):
    for i in range(len(caminho) - 1):
        if not existe_aresta(arestas, caminho[i], caminho[i + 1]):
            return False
    return True

def listar_vizinhos(vertices, arestas, vertice):
    print(f"Vizinhos de {vertice}: {vizinhos(vertices, arestas, vertice)}")

def exibir_grafo(vertices, arestas):
    print("Vértices:", vertices)
    print("Arestas:")
    for o, d in arestas:
        print(f"{o} -> {d}")

def main():
    vertices, arestas = criar_grafo()
    while True:
        print("\n1 - Mostrar Grafo\n2 - Inserir Vértice\n3 - Inserir Aresta\n4 - Remover Vértice\n5 - Remover Aresta\n6 - Grau dos Vértices\n7 - Verificar Aresta\n8 - Listar Vizinhos\n9 - Verificar Percurso\n0 - Sair")
        op = input("Escolha: ")
        if op == '1':
            exibir_grafo(vertices, arestas)
        elif op == '2':
            v = input("Vértice: ")
            inserir_vertice(vertices, v)
        elif op == '3':
            o, d = input("Origem Destino: ").split()
            inserir_aresta(vertices, arestas, o, d, True)
        elif op == '4':
            v = input("Vértice: ")
            remover_vertice(vertices, arestas, v)
        elif op == '5':
            o, d = input("Origem Destino: ").split()
            remover_aresta(arestas, o, d, True)
        elif op == '6':
            print(grau_vertices(vertices, arestas))
        elif op == '7':
            o, d = input("Origem Destino: ").split()
            print(existe_aresta(arestas, o, d))
        elif op == '8':
            v = input("Vértice: ")
            listar_vizinhos(vertices, arestas, v)
        elif op == '9':
            caminho = input("Caminho (v1 v2 ...): ").split()
            print(percurso_valido(arestas, caminho))
        elif op == '0':
            break

if __name__ == "__main__":
    main()
