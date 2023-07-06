# Declarando uma matriz (lista de listas)
matriz = [[1,2,3] , [4,5,6] , [7,8,9]]

# Imprimindo uma matriz (maneira padrão)
print(matriz)

# Imprimindo uma matriz (formatada)
for i in range (3):
    for j in range (3):
        print(matriz[i][j], end=" ")
    print()

# -------------------------------------------------------

# Declarando uma matriz (lista de listas) vazia
matriz = []

# Lendo os dados da matriz
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'matriz[{i}][{j}]: ')))
    matriz.append(linha)

# Mostrando a matriz
for i in range (3):
    print()
    for j in range (3):
        print(matriz[i][j], end=" ")