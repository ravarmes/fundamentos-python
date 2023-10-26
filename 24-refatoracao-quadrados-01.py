# Solução sem refatoração

# Entrada do usuário
n = int(input("Digite um número inteiro positivo: "))

quadrados = []
for i in range (1, n+1):
    quadrado = i ** 2
    quadrados.append(quadrado)

media = sum(quadrados) / len(quadrados)

numeros_maiores_media = []
for num in quadrados:
    if num > media:
        numeros_maiores_media.append(num)

for num in quadrados:
    if num < media:
        menor_proximo = num
    if num > media:
        mais_proximo = num
if (media - menor_proximo) < (mais_proximo - media):
    mais_proximo = menor_proximo
else:
    mais_proximo = mais_proximo


# Saída dos resultados
print("Quadrados dos números até", n, ":", quadrados)
print("Média dos quadrados:", media)
print("Números maiores que a média:", numeros_maiores_media)
print("Número mais próximo da média:", mais_proximo)
