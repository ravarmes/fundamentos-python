# Solução com refatoração

# Função para calcular a área
def calcular_area(comprimento, largura):
    return comprimento * largura

# Função para calcular o perímetro
def calcular_perimetro(comprimento, largura):
    return 2 * (comprimento + largura)

# Entradas
comprimento = 10
largura = 5

# Cálculo e saída usando as funções refatoradas
area = calcular_area(comprimento, largura)
perimetro = calcular_perimetro(comprimento, largura)

print("Área:", area)
print("Perímetro:", perimetro)
