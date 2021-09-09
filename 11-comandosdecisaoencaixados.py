#Comandos de Decisão Encaixados
#Classificação de Triângulos

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

#Testa a propriedade para verificar se é um triângulo
if (x + y > z) and (x + z > y) and (y + z > x):
    if (x == y) and (y == z):
        print("Triângulo Equilátero!")
    elif (x == y) or (x == z) or (y == z):
        print("Triângulo Isósceles!")
    else:
        print("Triângulo Escaleno!")
#Caso não seja triângulo
else:
    print("Os lados digitados não formam um triângulo!")
    

        