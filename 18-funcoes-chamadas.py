def mostrar_mensagem ( ): 
    print ("\nMensagem dentro da função")
    return

def calcular_produto (x , y , z):
    print ("\nProduto: ", ( x * y * z ))
    return

def calcular_quociente (a, b):
    quociente = a / b
    return quociente

# Chamada da função mostrar_mensagem
mostrar_mensagem()

# Chamada da função calcular_produto, passando 3 argumentos
calcular_produto(4, 7.5, 2.3)

# Chamada da função calcular_quociente, recebendo o retorno de um valor
q = calcular_quociente (124, 9)
print("\nQuociente: ", q)

