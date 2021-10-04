#Comandos de Decisão Não Aninhados
#Classificação de Triângulos

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))


if ((x + y > z) and (x + z > y) and (y + z > x)) and ((x == y) and (y == z)):
    print("Triângulo Equilátero!")
elif ((x + y > z) and (x + z > y) and (y + z > x)) and ((x == y) or (x == z) or (y == z)):
    print("Triângulo Isósceles!")
elif ((x + y > z) and (x + z > y) and (y + z > x)) and ((x != y) and (x != z) and (y != z)):
    print("Triângulo Escaleno!")
#Caso não seja triângulo
else:
    print("Os lados digitados não formam um triângulo!")


    