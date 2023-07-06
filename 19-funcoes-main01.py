# Função opcional main - exemplo 1 
# Note que a execução não começa aqui!

# Definição da função calcular_produto
# Recebe 3 valores, calcula o produto entre eles e o retorna 
def calcular_produto(a, b, c): 
    prod = a * b * c 
    return prod 

# Definição da função calcular_diferenca
# Recebe 2 valores, calcula a diferença entre eles e a retorna
def calcular_diferenca(a, b):
    dif = a - b 
    return dif 

# Ponto de entrada para o script 
# Verifica se __name__ é igual a "__main__" 
# Execução começa aqui! 
if (__name__ == "__main__"): 
    x = -9 
    y = -3 
    z = 6.98
    # Chamando as funções definidas 
    dif = calcular_diferenca(x, y) 
    prod = calcular_produto(x, y, z)   
    # Mostrando todos os valores ​
    print ("\nDentro do ponto de entrada do bloco if\n", 
           "\nDiferença = ", dif, 
           "\nProduto = ", prod)

