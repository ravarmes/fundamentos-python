def mostrar_mensagem ( ): 
    print ("\nMensagem dentro da função")
    
def calcular_produto (x , y , z):
    print ("\nProduto: ", ( x * y * z ))
    
def calcular_quociente (a, b):
    quociente = a / b
    return quociente

mostrar_mensagem()

calcular_produto(4, 7.5, 2.3)

q = calcular_quociente (124, 9)
print("\nQuociente: ", q)

