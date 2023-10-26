# Solução com refatoração

def calcular_quadrados_ate_n(n):
    quadrados = []
    for i in range (1, n+1):
        quadrado = i ** 2
        quadrados.append(quadrado)
    return quadrados

def calcular_media(quadrados):
    media = sum(quadrados) / len(quadrados)
    return media

def calcular_numeros_maiores_media(quadrados):
    media = calcular_media(quadrados)
    numeros_maiores_media = []
    for num in quadrados:
        if num > media:
            numeros_maiores_media.append(num)
    return numeros_maiores_media

def encontrar_numero_proximo_media(quadrados):
    media = calcular_media(quadrados)
    for num in quadrados:
        if num < media:
            menor_proximo = num
        if num > media:
            mais_proximo = num
    if (media - menor_proximo) < (mais_proximo - media):
        return menor_proximo
    else:
        return mais_proximo


# Entrada do usuário
n = int(input("Digite um número inteiro positivo: "))

# Calcula os quadrados até n
quadrados = calcular_quadrados_ate_n(n)

# Calcular média
media = calcular_media(quadrados)

# Calcular números maiores que a média
numeros_maiores_media = calcular_numeros_maiores_media(quadrados)

# Contar números maiores que a média
mais_proximo = encontrar_numero_proximo_media(quadrados)

# Saída dos resultados
print("Quadrados dos números até", n, ":", quadrados)
print("Média dos quadrados:", media)
print("Números maiores que a média:", numeros_maiores_media)
print("Número mais próximo da média:", mais_proximo)
